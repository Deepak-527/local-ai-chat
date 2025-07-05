#!/usr/bin/env python3
"""
KickGPT Web UI
A modern web interface for the Mistral 7B chat system
"""

from flask import Flask, render_template, request, jsonify, session
import requests
import json
import os
from datetime import datetime
import threading
import time

app = Flask(__name__)
app.secret_key = 'kickgpt-secret-key-2024'

# Configuration
API_BASE_URL = "http://localhost:5000"
DEFAULT_MODEL = "mistral-7b"

class ChatManager:
    def __init__(self):
        self.conversations = {}
    
    def get_conversation(self, session_id):
        if session_id not in self.conversations:
            self.conversations[session_id] = []
        return self.conversations[session_id]
    
    def add_message(self, session_id, role, content, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        conversation = self.get_conversation(session_id)
        message = {
            'role': role,
            'content': content,
            'timestamp': timestamp
        }
        conversation.append(message)
        return message
    
    def clear_conversation(self, session_id):
        self.conversations[session_id] = []

chat_manager = ChatManager()

def check_api_server():
    """Check if the API server is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/mistral/health", timeout=5)
        return response.status_code == 200
    except:
        return False

@app.route('/')
def index():
    """Main chat interface"""
    if 'session_id' not in session:
        session['session_id'] = f"session_{int(time.time())}"
    
    api_status = check_api_server()
    return render_template('chat.html', api_status=api_status)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        session_id = session.get('session_id')
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Add user message to conversation
        chat_manager.add_message(session_id, 'user', message)
        
        # Check if API server is running
        if not check_api_server():
            error_msg = "API server is not running. Please start it with: python api_server.py"
            chat_manager.add_message(session_id, 'assistant', error_msg)
            return jsonify({
                'response': error_msg,
                'error': 'API server unavailable'
            }), 503
        
        # Send request to API server
        try:
            api_response = requests.post(
                f"{API_BASE_URL}/mistral/chat",
                json={
                    'message': message,
                    'max_tokens': 500,
                    'temperature': 0.7
                },
                timeout=30
            )
            
            if api_response.status_code == 200:
                response_data = api_response.json()
                assistant_response = response_data.get('response', 'No response received')
                
                # Add assistant response to conversation
                chat_manager.add_message(session_id, 'assistant', assistant_response)
                
                return jsonify({
                    'response': assistant_response,
                    'conversation': chat_manager.get_conversation(session_id)
                })
            else:
                error_msg = f"API Error: {api_response.status_code}"
                chat_manager.add_message(session_id, 'assistant', error_msg)
                return jsonify({'response': error_msg, 'error': 'API error'}), 500
                
        except requests.exceptions.Timeout:
            error_msg = "Request timed out. Please try again."
            chat_manager.add_message(session_id, 'assistant', error_msg)
            return jsonify({'response': error_msg, 'error': 'timeout'}), 408
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Connection error: {str(e)}"
            chat_manager.add_message(session_id, 'assistant', error_msg)
            return jsonify({'response': error_msg, 'error': 'connection'}), 503
            
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/conversation', methods=['GET'])
def get_conversation():
    """Get current conversation"""
    session_id = session.get('session_id')
    return jsonify({
        'conversation': chat_manager.get_conversation(session_id)
    })

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    """Clear current conversation"""
    session_id = session.get('session_id')
    chat_manager.clear_conversation(session_id)
    return jsonify({'message': 'Conversation cleared'})

@app.route('/api/status')
def api_status():
    """Check API server status"""
    return jsonify({
        'api_running': check_api_server(),
        'api_url': API_BASE_URL
    })

if __name__ == '__main__':
    print("🌐 Starting KickGPT Web UI...")
    print(f"📡 API Server URL: {API_BASE_URL}")
    print("💡 Make sure to start the API server first: python api_server.py")
    print("🌍 Web UI will be available at: http://localhost:8081")
    
    app.run(host='0.0.0.0', port=8081, debug=True) 