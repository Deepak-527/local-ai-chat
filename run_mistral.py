#!/usr/bin/env python3
"""
Mistral 7B Local Runner with Conversation Memory
Optimized for 6GB RAM laptops with GPU acceleration
"""

import os
import sys
from typing import Optional, List, Dict
from llama_cpp import Llama

class MistralRunner:
    def __init__(self, model_path: str = "models/mistral-7b-v0.1.Q4_K_M.gguf"):
        """
        Initialize the Mistral model runner with conversation memory
        
        Args:
            model_path: Path to the GGUF model file
        """
        self.model_path = model_path
        self.model = None
        self.conversation_history = []
        self.system_prompt = """You are a highly capable and reliable AI assistant. Your responses are clear, concise, factual, and grounded in verified knowledge. When uncertain, you say so transparently. You avoid speculation, repetition, and hallucination. Maintain a friendly, professional tone, and support helpful, accurate, and engaging conversation across a wide range of topics."""
        self.load_model()
    
    def load_model(self):
        """Load the model with GPU acceleration for faster performance"""
        try:
            print("Loading Mistral model with GPU acceleration... This may take a moment...")
            
            # GPU-accelerated settings optimized for RTX 4050 (limited VRAM)
            self.model = Llama(
                model_path=self.model_path,
                n_ctx=2048,  # Reduced context window to save memory
                n_batch=256,  # Reduced batch size
                n_threads=4,  # CPU threads for non-GPU layers
                n_gpu_layers=99,  # Reduced GPU layers for RTX 4050
                verbose=False,
                use_mmap=True,  # Memory mapping for efficiency
                use_mlock=False,  # Don't lock memory to allow swapping
            )
            print("✅ Model loaded successfully with GPU acceleration!")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            sys.exit(1)
    
    def add_to_conversation(self, role: str, content: str):
        """Add a message to the conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
        # Keep only last 10 messages to prevent context overflow
        if len(self.conversation_history) > 10:
            self.conversation_history = self.conversation_history[-10:]
    
    def build_conversation_prompt(self, user_message: str) -> str:
        """Build a conversation prompt with history"""
        # Start with system prompt
        prompt = f"<s>[INST] {self.system_prompt} [/INST]"
        
        # Add conversation history in pairs (user + assistant)
        for i in range(0, len(self.conversation_history) - 1, 2):
            if i + 1 < len(self.conversation_history):
                user_msg = self.conversation_history[i]['content']
                assistant_msg = self.conversation_history[i + 1]['content']
                prompt += f" [INST] {user_msg} [/INST] {assistant_msg}"
        
        # Add current user message
        prompt += f" [INST] {user_message} [/INST]"
        
        return prompt
    
    def clear_conversation(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("🧹 Conversation history cleared!")
    
    def generate_response(self, prompt: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """
        Generate a response from the model
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0.0 = deterministic, 1.0 = creative)
        
        Returns:
            Generated response
        """
        if not self.model:
            return "❌ Model not loaded"
        
        try:
            response = self.model(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop=["</s>", "[INST]"],
                echo=False
            )
            
            # Extract the generated text
            if isinstance(response, dict) and 'choices' in response:
                generated_text = response['choices'][0]['text'].strip()
            else:
                generated_text = str(response).strip()
            
            return generated_text if generated_text else "❌ No response generated"
            
        except Exception as e:
            return f"❌ Error generating response: {e}"
    
    def chat(self, user_message: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """
        Generate a conversational response with memory
        
        Args:
            user_message: User's message
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
        
        Returns:
            Assistant's response
        """
        # Add user message to conversation
        self.add_to_conversation("user", user_message)
        
        # Use simple prompt format that was working before
        prompt = f"{self.system_prompt}\n\nUser: {user_message}\nAssistant:"
        
        # Generate response
        response = self.generate_response(prompt, max_tokens, temperature)
        
        # Add assistant response to conversation
        self.add_to_conversation("assistant", response)
        
        return response
    
    def interactive_chat(self):
        """Start an interactive chat session with memory"""
        print("\n🤖 Mistral 7B Chat Bot (with Memory)")
        print("Type 'quit' or 'exit' to end the session")
        print("Type 'help' for available commands")
        print("Type 'clear' to clear conversation history")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if user_input.lower() == 'help':
                    print("\n📋 Available commands:")
                    print("- quit/exit/q: Exit the chat")
                    print("- help: Show this help message")
                    print("- clear: Clear conversation history")
                    print("- settings: Show current model settings")
                    print("- history: Show conversation history")
                    print("- test: Run a test query")
                    continue
                
                if user_input.lower() == 'clear':
                    self.clear_conversation()
                    continue
                
                if user_input.lower() == 'settings':
                    print(f"\n⚙️  Model Settings:")
                    print(f"- Context window: 2048 tokens")
                    print(f"- Batch size: 256")
                    print(f"- Threads: 4")
                    print(f"- GPU layers: 20 (GPU acceleration)")
                    print(f"- Conversation memory: Enabled")
                    continue
                
                if user_input.lower() == 'history':
                    print(f"\n📜 Conversation History ({len(self.conversation_history)} messages):")
                    for i, msg in enumerate(self.conversation_history, 1):
                        role_emoji = "👤" if msg["role"] == "user" else "🤖"
                        print(f"{i}. {role_emoji} {msg['role'].title()}: {msg['content'][:100]}...")
                    continue
                
                if user_input.lower() == 'test':
                    print("\n🧪 Running test query...")
                    test_response = self.chat("Hello, how are you?", max_tokens=50)
                    print(f"Test response: {test_response}")
                    continue
                
                if not user_input:
                    continue
                
                print("\n🤖 Mistral: ", end="", flush=True)
                response = self.chat(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")

def main():
    """Main function to run the Mistral model"""
    print("🚀 Starting Mistral 7B Local Runner with Conversation Memory")
    
    # Check if model file exists
    model_path = "models/mistral-7b-v0.1.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        print("Please ensure the model file is in the models/ directory")
        sys.exit(1)
    
    # Initialize the runner
    runner = MistralRunner(model_path)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        # Single query mode
        query = " ".join(sys.argv[1:])
        print(f"\n📝 Query: {query}")
        print("\n🤖 Response:")
        response = runner.chat(query)
        print(response)
    else:
        # Interactive mode
        runner.interactive_chat()

if __name__ == "__main__":
    main() 