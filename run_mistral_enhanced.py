#!/usr/bin/env python3
"""
Enhanced Mistral 7B Runner with Prompt Templates
Uses structured prompts for better, more consistent responses
"""

import os
import sys
from typing import Optional
from run_mistral import MistralRunner
from prompt_templates import PromptTemplates, get_prompt, question, explain, code, write

class EnhancedMistralRunner(MistralRunner):
    """Enhanced Mistral runner with prompt templates"""
    
    def __init__(self, model_path: str = "models/mistral-7b-v0.1.Q4_K_M.gguf"):
        super().__init__(model_path)
    
    def ask_question(self, question_text: str, context: str = "", max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Ask a general question with structured prompt"""
        prompt = PromptTemplates.general_question(question_text, context)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def get_explanation(self, topic: str, level: str = "simple", max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Get an explanation with structured prompt"""
        prompt = PromptTemplates.explanation(topic, level)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def generate_code(self, language: str, task: str, requirements: str = "", max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Generate code with structured prompt"""
        prompt = PromptTemplates.code_generation(language, task, requirements)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def creative_write(self, genre: str, topic: str, length: str = "short", max_tokens: int = 512, temperature: float = 0.7) -> str:
        """Generate creative writing with structured prompt"""
        prompt = PromptTemplates.creative_writing(genre, topic, length)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def analyze_text(self, text: str, analysis_type: str = "general", max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Analyze text with structured prompt"""
        prompt = PromptTemplates.analysis(text, analysis_type)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def compare_items(self, item1: str, item2: str, criteria: str = "", max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Compare items with structured prompt"""
        prompt = PromptTemplates.comparison(item1, item2, criteria)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def solve_problem(self, problem: str, approach: str = "step-by-step", max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Solve problems with structured prompt"""
        prompt = PromptTemplates.problem_solving(problem, approach)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def summarize_text(self, text: str, length: str = "brief", max_tokens: int = 512, temperature: float = 0.2) -> str:
        """Summarize text with structured prompt"""
        prompt = PromptTemplates.summarization(text, length)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def brainstorm_ideas(self, topic: str, num_ideas: int = 5, max_tokens: int = 512, temperature: float = 0.8) -> str:
        """Brainstorm ideas with structured prompt"""
        prompt = PromptTemplates.brainstorming(topic, num_ideas)
        return self.generate_response(prompt, max_tokens, temperature)
    
    def follow_instruction(self, instruction: str, context: str = "", max_tokens: int = 512, temperature: float = 0.3) -> str:
        """Follow specific instructions with structured prompt"""
        prompt = PromptTemplates.instruction_following(instruction, context)
        return self.generate_response(prompt, max_tokens, temperature)

def interactive_enhanced_chat():
    """Enhanced interactive chat with prompt templates"""
    print("\n🤖 Enhanced Mistral 7B Chat Bot")
    print("Type 'help' for available commands")
    print("Type 'quit' or 'exit' to end the session")
    print("-" * 50)
    
    runner = EnhancedMistralRunner()
    
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
                print("- templates: Show available prompt templates")
                print("- question <text>: Ask a general question")
                print("- explain <topic>: Get an explanation")
                print("- code <language> <task>: Generate code")
                print("- write <genre> <topic>: Creative writing")
                print("- analyze <text>: Analyze text")
                print("- compare <item1> vs <item2>: Compare items")
                print("- solve <problem>: Solve a problem")
                print("- summarize <text>: Summarize text")
                print("- brainstorm <topic>: Brainstorm ideas")
                continue
            
            if user_input.lower() == 'templates':
                print("\n🎯 Available Prompt Templates:")
                print("1. question <text> - Ask general questions")
                print("2. explain <topic> - Get explanations")
                print("3. code <language> <task> - Generate code")
                print("4. write <genre> <topic> - Creative writing")
                print("5. analyze <text> - Text analysis")
                print("6. compare <item1> vs <item2> - Comparisons")
                print("7. solve <problem> - Problem solving")
                print("8. summarize <text> - Text summarization")
                print("9. brainstorm <topic> - Brainstorming")
                continue
            
            # Parse template commands
            if user_input.lower().startswith('question '):
                question_text = user_input[9:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.ask_question(question_text)
                print(response)
                continue
            
            if user_input.lower().startswith('explain '):
                topic = user_input[8:].strip()
                print("\n🤖 Mistral: ", end="", flush=True)
                response = runner.get_explanation(topic)
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
    """Main function for enhanced Mistral runner"""
    print("🚀 Starting Enhanced Mistral 7B Runner")
    
    # Check if model file exists
    model_path = "models/mistral-7b-v0.1.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        print("Please ensure the model file is in the models/ directory")
        sys.exit(1)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        # Single query mode with enhanced prompts
        query = " ".join(sys.argv[1:])
        print(f"\n📝 Query: {query}")
        print("\n🤖 Response:")
        
        runner = EnhancedMistralRunner(model_path)
        response = runner.ask_question(query)
        print(response)
    else:
        # Interactive mode
        interactive_enhanced_chat()

if __name__ == "__main__":
    main() 