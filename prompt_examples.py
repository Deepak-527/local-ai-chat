#!/usr/bin/env python3
"""
Prompt Examples for Mistral 7B
Demonstrates all the different simple prompt types
"""

from simple_enhanced import SimpleEnhancedRunner
from simple_prompts import SimplePrompts

def run_prompt_examples():
    """Run examples of all prompt types"""
    
    print("🚀 Mistral 7B Prompt Examples")
    print("=" * 60)
    
    # Initialize the runner
    print("Loading model...")
    runner = SimpleEnhancedRunner()
    
    examples = [
        {
            "type": "Question",
            "prompt": "What is artificial intelligence?",
            "method": runner.ask_question,
            "args": ["What is artificial intelligence?"]
        },
        {
            "type": "Explanation",
            "prompt": "Explain machine learning",
            "method": runner.explain_topic,
            "args": ["machine learning"]
        },
        {
            "type": "Code Generation",
            "prompt": "Python function to calculate factorial",
            "method": runner.generate_code,
            "args": ["Python", "calculate factorial"]
        },
        {
            "type": "Creative Writing",
            "prompt": "Science fiction story about time travel",
            "method": runner.creative_write,
            "args": ["science fiction", "time travel"]
        },
        {
            "type": "Text Analysis",
            "prompt": "Analyze: 'AI is transforming the world'",
            "method": runner.analyze_text,
            "args": ["AI is transforming the world"]
        },
        {
            "type": "Comparison",
            "prompt": "Compare Python vs JavaScript",
            "method": runner.compare_items,
            "args": ["Python", "JavaScript"]
        },
        {
            "type": "Problem Solving",
            "prompt": "How to improve website performance",
            "method": runner.solve_problem,
            "args": ["improve website performance"]
        },
        {
            "type": "Summarization",
            "prompt": "Summarize a long text about technology",
            "method": runner.summarize_text,
            "args": ["Technology has evolved rapidly over the past few decades, transforming how we live, work, and communicate. From the internet to smartphones to artificial intelligence, technological advancements have created new opportunities and challenges for society."]
        },
        {
            "type": "Brainstorming",
            "prompt": "Creative uses for AI in education",
            "method": runner.brainstorm_ideas,
            "args": ["creative uses for AI in education"]
        },
        {
            "type": "Definition",
            "prompt": "Define blockchain",
            "method": runner.get_definition,
            "args": ["blockchain"]
        },
        {
            "type": "Example",
            "prompt": "Example of machine learning application",
            "method": runner.get_example,
            "args": ["machine learning application"]
        },
        {
            "type": "Tips",
            "prompt": "Tips for learning programming",
            "method": runner.get_tips,
            "args": ["learning programming"]
        },
        {
            "type": "Pros and Cons",
            "prompt": "Pros and cons of remote work",
            "method": runner.get_pros_cons,
            "args": ["remote work"]
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{'='*60}")
        print(f"Example {i}: {example['type']}")
        print(f"{'='*60}")
        print(f"Prompt: {example['prompt']}")
        print("\n🤖 Response:")
        
        try:
            response = example['method'](*example['args'])
            print(response)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("\n" + "-"*40)
    
    print("\n✅ All prompt examples completed!")

def show_prompt_templates():
    """Show all available prompt templates"""
    print("\n🎯 Available Simple Prompt Templates:")
    print("=" * 50)
    
    templates = [
        ("Question", "q(text)", "Ask a simple question"),
        ("Explanation", "e(topic)", "Explain a topic simply"),
        ("Code Generation", "c(language, task)", "Generate code with comments"),
        ("Creative Writing", "w(genre, topic)", "Write creative content"),
        ("Text Analysis", "a(text)", "Analyze text"),
        ("Comparison", "comp(item1, item2)", "Compare two items"),
        ("Problem Solving", "s(problem)", "Solve a problem"),
        ("Summarization", "sum(text)", "Summarize text"),
        ("Brainstorming", "b(topic)", "Generate creative ideas"),
        ("Definition", "SimplePrompts.definition(term)", "Get definition"),
        ("Example", "SimplePrompts.example(concept)", "Get example"),
        ("Tips", "SimplePrompts.tips(topic)", "Get tips"),
        ("Pros/Cons", "SimplePrompts.pros_cons(topic)", "Get pros and cons"),
        ("How-to", "SimplePrompts.how_to(task)", "Get how-to instructions"),
        ("Fact Check", "SimplePrompts.fact_check(statement)", "Check if statement is true"),
        ("Step-by-step", "SimplePrompts.step_by_step(instruction)", "Follow instructions"),
        ("List Items", "SimplePrompts.list_items(category, count)", "List items"),
        ("Why", "SimplePrompts.why(question)", "Ask why"),
        ("What-if", "SimplePrompts.what_if(scenario)", "Ask what-if"),
        ("Best Practice", "SimplePrompts.best_practice(topic)", "Get best practices"),
        ("Common Mistakes", "SimplePrompts.common_mistakes(topic)", "Get common mistakes")
    ]
    
    for i, (name, usage, description) in enumerate(templates, 1):
        print(f"{i:2d}. {name:15} | {usage:35} | {description}")
    
    print(f"\nTotal: {len(templates)} prompt templates available")

def interactive_demo():
    """Interactive demo of prompt templates"""
    print("\n🎮 Interactive Prompt Demo")
    print("Type a prompt type to see it in action:")
    print("- question, explain, code, write, analyze")
    print("- compare, solve, summarize, brainstorm")
    print("- define, example, tips, pros_cons")
    print("- quit to exit")
    
    runner = SimpleEnhancedRunner()
    
    while True:
        try:
            user_input = input("\n👤 Enter prompt type: ").strip().lower()
            
            if user_input in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input == 'question':
                text = input("Enter question: ")
                print("\n🤖 Response:")
                print(runner.ask_question(text))
            
            elif user_input == 'explain':
                topic = input("Enter topic to explain: ")
                print("\n🤖 Response:")
                print(runner.explain_topic(topic))
            
            elif user_input == 'code':
                language = input("Enter programming language: ")
                task = input("Enter coding task: ")
                print("\n🤖 Response:")
                print(runner.generate_code(language, task))
            
            elif user_input == 'write':
                genre = input("Enter genre: ")
                topic = input("Enter topic: ")
                print("\n🤖 Response:")
                print(runner.creative_write(genre, topic))
            
            elif user_input == 'analyze':
                text = input("Enter text to analyze: ")
                print("\n🤖 Response:")
                print(runner.analyze_text(text))
            
            elif user_input == 'compare':
                item1 = input("Enter first item: ")
                item2 = input("Enter second item: ")
                print("\n🤖 Response:")
                print(runner.compare_items(item1, item2))
            
            elif user_input == 'solve':
                problem = input("Enter problem: ")
                print("\n🤖 Response:")
                print(runner.solve_problem(problem))
            
            elif user_input == 'summarize':
                text = input("Enter text to summarize: ")
                print("\n🤖 Response:")
                print(runner.summarize_text(text))
            
            elif user_input == 'brainstorm':
                topic = input("Enter topic to brainstorm: ")
                print("\n🤖 Response:")
                print(runner.brainstorm_ideas(topic))
            
            elif user_input == 'define':
                term = input("Enter term to define: ")
                print("\n🤖 Response:")
                print(runner.get_definition(term))
            
            elif user_input == 'example':
                concept = input("Enter concept for example: ")
                print("\n🤖 Response:")
                print(runner.get_example(concept))
            
            elif user_input == 'tips':
                topic = input("Enter topic for tips: ")
                print("\n🤖 Response:")
                print(runner.get_tips(topic))
            
            elif user_input == 'pros_cons':
                topic = input("Enter topic for pros/cons: ")
                print("\n🤖 Response:")
                print(runner.get_pros_cons(topic))
            
            else:
                print("❌ Unknown prompt type. Type 'help' for available types.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🤖 Mistral 7B Prompt Examples")
    print("This demonstrates effective prompt templates for better responses")
    
    try:
        # Show available templates
        show_prompt_templates()
        
        # Ask user what they want to do
        print("\nWhat would you like to do?")
        print("1. Run all examples")
        print("2. Interactive demo")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            run_prompt_examples()
        elif choice == "2":
            interactive_demo()
        elif choice == "3":
            print("👋 Goodbye!")
        else:
            print("Invalid choice. Running all examples...")
            run_prompt_examples()
            
    except Exception as e:
        print(f"❌ Error: {e}") 