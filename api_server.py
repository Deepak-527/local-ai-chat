#!/usr/bin/env python3
"""
Mistral 7B API Server with Swagger Documentation
Provides REST API endpoints for the Mistral model
"""

import os
import sys
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from run_mistral import MistralRunner
import threading
import time

# Initialize Flask app
app = Flask(__name__)
api = Api(app, 
    title='Mistral 7B API',
    version='1.0',
    description='A REST API for the Mistral 7B language model',
    doc='/docs',
    default='mistral',
    default_label='Mistral 7B Model Endpoints'
)

# Create namespace for our API
ns = api.namespace('mistral', description='Mistral 7B model operations')

# Define request/response models for Swagger documentation
request_model = api.model('Request', {
    'prompt': fields.String(required=True, description='Input prompt'),
    'max_tokens': fields.Integer(default=512, description='Max tokens to generate'),
    'temperature': fields.Float(default=0.2, description='Sampling temperature')
})

response_model = api.model('Response', {
    'success': fields.Boolean(description='Request success'),
    'response': fields.String(description='Generated text'),
    'error': fields.String(description='Error message if any')
})

health_model = api.model('HealthResponse', {
    'status': fields.String(description='Service status'),
    'model_loaded': fields.Boolean(description='Whether the model is loaded'),
    'uptime': fields.String(description='Service uptime')
})

# Global variables
model_runner = None
model_loading = False
start_time = time.time()

def load_model():
    """Load the model in a separate thread"""
    global model_runner, model_loading
    try:
        model_loading = True
        model_runner = MistralRunner()
        model_loading = False
        print("✅ Model loaded in API server!")
    except Exception as e:
        model_loading = False
        print(f"❌ Error loading model: {e}")

# Start model loading in background
model_thread = threading.Thread(target=load_model)
model_thread.daemon = True
model_thread.start()

@ns.route('/generate')
class GenerateResource(Resource):
    @ns.doc('generate_text')
    @ns.expect(request_model)
    @ns.marshal_with(response_model)
    def post(self):
        """Generate text using Mistral model"""
        try:
            if model_loading:
                return {'success': False, 'response': '', 'error': 'Model loading...'}, 503
            
            if not model_runner or not model_runner.model:
                return {'success': False, 'response': '', 'error': 'Model not loaded'}, 503
            
            data = request.get_json()
            if not data or 'prompt' not in data:
                return {'success': False, 'response': '', 'error': 'Prompt required'}, 400
            
            prompt = data['prompt']
            max_tokens = data.get('max_tokens', 512)
            temperature = data.get('temperature', 0.2)
            print(f"Prompt: {prompt}")
            response = model_runner.generate_response(prompt, max_tokens, temperature)
            
            if response.startswith('❌'):
                return {'success': False, 'response': '', 'error': response}, 500
            
            return {'success': True, 'response': response, 'error': None}
            
        except Exception as e:
            return {'success': False, 'response': '', 'error': str(e)}, 500

@ns.route('/health')
class HealthResource(Resource):
    @ns.doc('health_check')
    @ns.marshal_with(health_model)
    def get(self):
        """Check the health status of the API and model"""
        uptime = time.time() - start_time
        uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s"
        
        return {
            'status': 'healthy' if model_runner and model_runner.model else 'loading',
            'model_loaded': model_runner is not None and model_runner.model is not None,
            'uptime': uptime_str
        }

@ns.route('/chat')
class ChatResource(Resource):
    @ns.doc('chat_completion')
    @ns.expect(request_model)
    @ns.marshal_with(response_model)
    def post(self):
        """Generate a chat-style response with conversation memory"""
        try:
            if model_loading:
                return {'success': False, 'response': '', 'error': 'Model loading...'}, 503
            
            if not model_runner or not model_runner.model:
                return {'success': False, 'response': '', 'error': 'Model not loaded'}, 503
            
            data = request.get_json()
            if not data or 'message' not in data:
                return {'success': False, 'response': '', 'error': 'Message required'}, 400
            
            message = data['message']
            max_tokens = data.get('max_tokens', 512)
            temperature = data.get('temperature', 0.2)
            print(f"Chat message: {message}")
            
            # Use the new chat method with conversation memory
            response = model_runner.chat(message, max_tokens, temperature)
            
            if response.startswith('❌'):
                return {'success': False, 'response': '', 'error': response}, 500
            
            return {'success': True, 'response': response, 'error': None}
            
        except Exception as e:
            return {'success': False, 'response': '', 'error': str(e)}, 500

@ns.route('/clear')
class ClearResource(Resource):
    @ns.doc('clear_conversation')
    def post(self):
        """Clear the conversation history"""
        try:
            if model_runner:
                model_runner.clear_conversation()
            return {'success': True, 'message': 'Conversation cleared'}, 200
        except Exception as e:
            return {'success': False, 'error': str(e)}, 500

@ns.route('/conversation')
class ConversationResource(Resource):
    @ns.doc('get_conversation')
    def get(self):
        """Get the current conversation history"""
        try:
            if model_runner:
                return {
                    'success': True, 
                    'conversation': model_runner.conversation_history
                }, 200
            else:
                return {'success': False, 'conversation': []}, 200
        except Exception as e:
            return {'success': False, 'error': str(e)}, 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found. Check /docs for available endpoints.'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("🚀 Starting Mistral 7B API Server")
    print("📚 Swagger documentation available at: http://localhost:5000/docs")
    print("🔍 Health check available at: http://localhost:5000/mistral/health")
    
    # Check if model file exists
    model_path = "models/mistral-7b-v0.1.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        print("Please ensure the model file is in the models/ directory")
        sys.exit(1)
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True) 