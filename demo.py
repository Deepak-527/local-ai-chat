#!/usr/bin/env python3
"""
KickGPT Demo - Showcase All Features
Demonstrates the complete Mistral 7B local runner with enhanced prompts
"""

import os
import sys
from simple_enhanced import SimpleEnhancedRunner

def main():
    """Main demo function"""
    print("🚀 KickGPT - Mistral 7B Local Runner Demo")
    print("=" * 60)
    print("This demo showcases all features of the enhanced Mistral system")
    print("=" * 60)
    
    # Check if model exists
    model_path = "models/mistral-7b-v0.1.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"❌ Model file not found at: {model_path}")
        print("Please ensure the model file is in the models/ directory")
        return
    
    print("\n📋 Available Features:")
    print("1. Basic Mistral Runner (run_mistral.py)")
    print("2. Enhanced Prompts (simple_enhanced.py) - RECOMMENDED")
    print("3. REST API Server (api_server.py)")
    print("4. Web UI (web_ui.py) - NEW!")
    print("5. Prompt Examples (prompt_examples.py)")
    print("6. Interactive Demo")
    print("7. Exit")
    
    while True:
        try:
            choice = input("\n🎯 Select a feature (1-7): ").strip()
            
            if choice == "1":
                print("\n🔧 Basic Mistral Runner")
                print("Run: python run_mistral.py")
                print("Features: Basic chat, single queries")
                
            elif choice == "2":
                print("\n✨ Enhanced Prompts (RECOMMENDED)")
                print("Run: python simple_enhanced.py")
                print("Features: 20+ prompt templates, better responses")
                demo_enhanced_prompts()
                
            elif choice == "3":
                print("\n🌐 REST API Server")
                print("Run: python api_server.py")
                print("Features: HTTP API, Swagger docs, JSON responses")
                
            elif choice == "4":
                print("\n🌐 Web UI (NEW!)")
                print("Run: python start_web_ui.py")
                print("Features: Beautiful web interface, real-time chat")
                print("Access: http://localhost:8081")
                demo_web_ui()
                
            elif choice == "5":
                print("\n📝 Prompt Examples")
                print("Run: python prompt_examples.py")
                print("Features: All prompt types demonstrated")
                
            elif choice == "6":
                print("\n🎮 Interactive Demo")
                interactive_demo()
                
            elif choice == "7":
                print("👋 Thanks for trying KickGPT!")
                break
                
            else:
                print("❌ Invalid choice. Please select 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def demo_enhanced_prompts():
    """Demo the enhanced prompt system"""
    print("\n🎯 Enhanced Prompt Templates Demo")
    print("=" * 50)
    
    try:
        runner = SimpleEnhancedRunner()
        
        demos = [
            ("Question", "What is artificial intelligence?", runner.ask_question),
            ("Explanation", "machine learning", runner.explain_topic),
            ("Code Generation", ("Python", "create a simple web scraper"), runner.generate_code),
            ("Creative Writing", ("science fiction", "time travel"), runner.creative_write),
            ("Comparison", ("Python", "JavaScript"), runner.compare_items),
            ("Problem Solving", "improve website performance", runner.solve_problem),
            ("Definition", "blockchain", runner.get_definition),
            ("Tips", "learning programming", runner.get_tips)
        ]
        
        for i, (prompt_type, args, method) in enumerate(demos, 1):
            print(f"\n{i}. {prompt_type}")
            print("-" * 30)
            
            if isinstance(args, tuple):
                response = method(*args)
            else:
                response = method(args)
            
            # Show first 200 characters of response
            preview = response[:200] + "..." if len(response) > 200 else response
            print(f"Response: {preview}")
            
        print(f"\n✅ Demo completed! {len(demos)} prompt types shown.")
        
    except Exception as e:
        print(f"❌ Error in demo: {e}")

def interactive_demo():
    """Interactive demo with user input"""
    print("\n🎮 Interactive Demo")
    print("=" * 30)
    print("Try different prompt types interactively!")
    print("Type 'help' for available commands, 'quit' to exit")
    
    try:
        runner = SimpleEnhancedRunner()
        
        while True:
            user_input = input("\n👤 Enter command: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if user_input.lower() == 'help':
                print("\n📋 Available Commands:")
                print("- question <text> - Ask a question")
                print("- explain <topic> - Explain a topic")
                print("- code <language> <task> - Generate code")
                print("- write <genre> <topic> - Creative writing")
                print("- compare <item1> vs <item2> - Compare items")
                print("- solve <problem> - Solve a problem")
                print("- define <term> - Get definition")
                print("- tips <topic> - Get tips")
                print("- quit - Exit demo")
                continue
            
            # Parse commands
            if user_input.lower().startswith('question '):
                question_text = user_input[9:].strip()
                print("\n🤖 Response:")
                print(runner.ask_question(question_text))
                
            elif user_input.lower().startswith('explain '):
                topic = user_input[8:].strip()
                print("\n🤖 Response:")
                print(runner.explain_topic(topic))
                
            elif user_input.lower().startswith('code '):
                parts = user_input[5:].strip().split(' ', 1)
                if len(parts) >= 2:
                    language, task = parts[0], parts[1]
                    print("\n🤖 Response:")
                    print(runner.generate_code(language, task))
                else:
                    print("❌ Usage: code <language> <task>")
                    
            elif user_input.lower().startswith('write '):
                parts = user_input[6:].strip().split(' ', 1)
                if len(parts) >= 2:
                    genre, topic = parts[0], parts[1]
                    print("\n🤖 Response:")
                    print(runner.creative_write(genre, topic))
                else:
                    print("❌ Usage: write <genre> <topic>")
                    
            elif user_input.lower().startswith('compare '):
                if ' vs ' in user_input:
                    parts = user_input[8:].strip().split(' vs ', 1)
                    item1, item2 = parts[0], parts[1]
                    print("\n🤖 Response:")
                    print(runner.compare_items(item1, item2))
                else:
                    print("❌ Usage: compare <item1> vs <item2>")
                    
            elif user_input.lower().startswith('solve '):
                problem = user_input[6:].strip()
                print("\n🤖 Response:")
                print(runner.solve_problem(problem))
                
            elif user_input.lower().startswith('define '):
                term = user_input[7:].strip()
                print("\n🤖 Response:")
                print(runner.get_definition(term))
                
            elif user_input.lower().startswith('tips '):
                topic = user_input[5:].strip()
                print("\n🤖 Response:")
                print(runner.get_tips(topic))
                
            else:
                print("❌ Unknown command. Type 'help' for available commands.")
                
    except Exception as e:
        print(f"❌ Error in interactive demo: {e}")

def demo_web_ui():
    """Demo the web UI functionality"""
    print("\n🌐 Web UI Demo")
    print("=" * 40)
    print("The web UI provides a beautiful, modern chat interface!")
    print("\n🚀 To start the web UI:")
    print("1. Run: python start_web_ui.py")
    print("2. Open browser to: http://localhost:8081")
    print("3. Start chatting!")
    
    print("\n✨ Web UI Features:")
    print("- Beautiful gradient design")
    print("- Real-time chat with typing indicators")
    print("- Conversation history")
    print("- Mobile responsive")
    print("- Auto-resizing text area")
    print("- Clear chat functionality")
    print("- API status indicator")
    
    print("\n🔧 Alternative startup:")
    print("Terminal 1: python api_server.py")
    print("Terminal 2: python web_ui.py")
    
    print("\n📱 Access URLs:")
    print("- Web UI: http://localhost:8081")
    print("- API Server: http://localhost:5000")
    print("- API Docs: http://localhost:5000/")

if __name__ == "__main__":
    main() 