#!/usr/bin/env python3
"""
Simple Enhanced Mistral 7B Runner
Uses simple, effective prompt templates for better responses
"""

import os
import sys
from run_mistral import MistralRunner
from simple_prompts import SimplePrompts, q, e, c, w, a, comp, s, sum, b

class SimpleEnhancedRunner(MistralRunner):
    """Simple enhanced Mistral runner with effective prompts"""
    
    def __init__(self, model_path: str = "models/mistral-7b-v0.1.Q4_K_M.gguf"):
        super().__init__(model_path)
    
    def ask_question(self, question_text: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Ask a question with simple prompt"""
        prompt = SimplePrompts.question(question_text)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def explain_topic(self, topic: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Explain a topic with simple prompt"""
        prompt = SimplePrompts.explain(topic)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def generate_code(self, language: str, task: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Generate code with simple prompt"""
        prompt = SimplePrompts.code(language, task)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def creative_write(self, genre: str, topic: str, max_tokens: int = 512, temperature: float = 0.7) -> str:
        """Creative writing with simple prompt"""
        prompt = SimplePrompts.write(genre, topic)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def analyze_text(self, text: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Analyze text with simple prompt"""
        prompt = SimplePrompts.analyze(text)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def compare_items(self, item1: str, item2: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Compare items with simple prompt"""
        prompt = SimplePrompts.compare(item1, item2)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def solve_problem(self, problem: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Solve problem with simple prompt"""
        prompt = SimplePrompts.solve(problem)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def summarize_text(self, text: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Summarize text with simple prompt"""
        prompt = SimplePrompts.summarize(text)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def brainstorm_ideas(self, topic: str, max_tokens: int = 512, temperature: float = 0.8) -> str:
        """Brainstorm ideas with simple prompt"""
        prompt = SimplePrompts.brainstorm(topic)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def get_definition(self, term: str, max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Get definition with simple prompt"""
        prompt = SimplePrompts.definition(term)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def get_example(self, concept: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Get example with simple prompt"""
        prompt = SimplePrompts.example(concept)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def get_tips(self, topic: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Get tips with simple prompt"""
        prompt = SimplePrompts.tips(topic)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def get_pros_cons(self, topic: str, max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Get pros and cons with simple prompt"""
        prompt = SimplePrompts.pros_cons(topic)
        return self.generate_response(prompt, max_tokens, temperature)

def interactive_simple_chat():
    """Interactive chat with simple prompts"""
    print("\n🤖 Simple Enhanced Mistral 7B Chat Bot")
    print("Type 'help' for available commands")
    print("Type 'quit' or 'exit' to end the session")
    print("-" * 50)
    
    runner = SimpleEnhancedRunner()
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input.lower() == 'help':
                print("\n📋 Available Commands:")
                print("- quit/exit/q: Exit the chat")
                print("- help: Show this help message")
                print("- question <text>: Ask a question")
                print("- explain <topic>: Explain a topic")
                print("- code <language> <task>: Generate code")
                print("- write <genre> <topic>: Creative writing")
                print("- analyze <text>: Analyze text")
                print("- compare <item1> vs <item2>: Compare items")
                print("- solve <problem>: Solve a problem")
                print("- summarize <text>: Summarize text")
                print("- brainstorm <topic>: Brainstorm ideas")
                print("- define <term>: Get definition")
                print("- example <concept>: Get example")
                print("- tips <topic>: Get tips")
                print("- pros_cons <topic>: Get pros and cons")
                continue
            
            # Parse commands
            if user_input.lower().startswith('question '):
                question_text = user_input[9:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.ask_question(question_text)
                print(response)
                continue
            
            if user_input.lower().startswith('explain '):
                topic = user_input[8:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.explain_topic(topic)
                print(response)
                continue
            
            if user_input.lower().startswith('code '):
                parts = user_input[5:].strip().split(' ', 1)
                if len(parts) >= 2:
                    language, task = parts[0], parts[1]
                    print("\n🤖 Mistral: ", end="", flush=True)
                    response = runner.generate_code(language, task)
                    print(response)
                else:
                    print("❌ Usage: code <language> <task>")
                continue
            
            if user_input.lower().startswith('write '):
                parts = user_input[6:].strip().split(' ', 1)
                if len(parts) >= 2:
                    genre, topic = parts[0], parts[1]
                    print("\n🤖 Mistral: ", end="", flush=True)
                    response = runner.creative_write(genre, topic)
                    print(response)
                else:
                    print("❌ Usage: write <genre> <topic>")
                continue
            
            if user_input.lower().startswith('analyze '):
                text = user_input[8:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.analyze_text(text)
                print(response)
                continue
            
            if user_input.lower().startswith('compare '):
                if ' vs ' in user_input:
                    parts = user_input[8:].strip().split(' vs ', 1)
                    item1, item2 = parts[0], parts[1]
                    print("\n🤖 Mistral: ", end="", flush=True)
                    response = runner.compare_items(item1, item2)
                    print(response)
                else:
                    print("❌ Usage: compare <item1> vs <item2>")
                continue
            
            if user_input.lower().startswith('solve '):
                problem = user_input[6:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.solve_problem(problem)
                print(response)
                continue
            
            if user_input.lower().startswith('summarize '):
                text = user_input[10:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.summarize_text(text)
                print(response)
                continue
            
            if user_input.lower().startswith('brainstorm '):
                topic = user_input[11:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.brainstorm_ideas(topic)
                print(response)
                continue
            
            if user_input.lower().startswith('define '):
                term = user_input[7:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.get_definition(term)
                print(response)
                continue
            
            if user_input.lower().startswith('example '):
                concept = user_input[8:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.get_example(concept)
                print(response)
                continue
            
            if user_input.lower().startswith('tips '):
                topic = user_input[5:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.get_tips(topic)
                print(response)
                continue
            
            if user_input.lower().startswith('pros_cons '):
                topic = user_input[10:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.get_pros_cons(topic)
                print(response)
                continue
            
            # Default: treat as general question
            if user_input:
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.ask_question(user_input)
                print(response)
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

def main():
    """Main function for simple enhanced Mistral runner"""
    print("🚀 Starting Simple Enhanced Mistral 7B Runner")
    
    # Check if model file exists
    model_path = "models/mistral-7b-v0.1.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        print("Please ensure the model file is in the models/ directory")
        sys.exit(1)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        # Single query mode with simple prompts
        query = " ".join(sys.argv[1:])
        print(f"\n📝 Query: {query}")
        print("\n🤖 Response:")
        
        runner = SimpleEnhancedRunner(model_path)
        response = runner.ask_question(query)
        print(response)
    else:
        # Interactive mode
        interactive_simple_chat()

if __name__ == "__main__":
    main() 