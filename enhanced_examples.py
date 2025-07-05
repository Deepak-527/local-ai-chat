#!/usr/bin/env python3
"""
Enhanced Examples for Mistral 7B
Demonstrates the improved prompt templates for better responses
"""

from run_mistral_enhanced import EnhancedMistralRunner
from prompt_templates import PromptTemplates

def demonstrate_enhanced_prompts():
    """Demonstrate various enhanced prompt templates"""
    
    print("🚀 Enhanced Mistral 7B Examples")
    print("=" * 60)
    
    # Initialize the enhanced runner
    print("Loading enhanced model...")
    runner = EnhancedMistralRunner()
    
    # Example 1: General Question with Context
    print("\n" + "="*60)
    print("Example 1: General Question with Context")
    print("="*60)
    
    context = "You are a helpful AI assistant with expertise in technology and science."
    question = "What is the difference between AI and machine learning?"
    
    print(f"Context: {context}")
    print(f"Question: {question}")
    print("\n🤖 Response:")
    response = runner.ask_question(question, context, max_tokens=200)
    print(response)
    
    # Example 2: Detailed Explanation
    print("\n" + "="*60)
    print("Example 2: Detailed Explanation")
    print("="*60)
    
    print("Topic: Quantum Computing")
    print("Level: Detailed")
    print("\n🤖 Response:")
    response = runner.get_explanation("quantum computing", level="detailed", max_tokens=300)
    print(response)
    
    # Example 3: Code Generation
    print("\n" + "="*60)
    print("Example 3: Code Generation")
    print("="*60)
    
    print("Language: Python")
    print("Task: Create a function to sort a list of dictionaries by a specific key")
    print("Requirements: Include error handling and documentation")
    print("\n🤖 Response:")
    response = runner.generate_code(
        "Python", 
        "create a function to sort a list of dictionaries by a specific key",
        "Include error handling and documentation",
        max_tokens=250
    )
    print(response)
    
    # Example 4: Creative Writing
    print("\n" + "="*60)
    print("Example 4: Creative Writing")
    print("="*60)
    
    print("Genre: Science Fiction")
    print("Topic: A robot discovering emotions")
    print("Length: Medium")
    print("\n🤖 Response:")
    response = runner.creative_write("science fiction", "a robot discovering emotions", "medium", max_tokens=400)
    print(response)
    
    # Example 5: Text Analysis
    print("\n" + "="*60)
    print("Example 5: Text Analysis")
    print("="*60)
    
    text_to_analyze = "Artificial intelligence is transforming the way we live and work. From virtual assistants to autonomous vehicles, AI technologies are becoming increasingly integrated into our daily lives."
    
    print(f"Text to analyze: {text_to_analyze}")
    print("Analysis type: Critical")
    print("\n🤖 Response:")
    response = runner.analyze_text(text_to_analyze, "critical", max_tokens=200)
    print(response)
    
    # Example 6: Comparison
    print("\n" + "="*60)
    print("Example 6: Comparison")
    print("="*60)
    
    print("Comparing: Python vs JavaScript")
    print("Criteria: Ease of learning, job market, versatility")
    print("\n🤖 Response:")
    response = runner.compare_items("Python", "JavaScript", "ease of learning, job market, versatility", max_tokens=300)
    print(response)
    
    # Example 7: Problem Solving
    print("\n" + "="*60)
    print("Example 7: Problem Solving")
    print("="*60)
    
    problem = "How to optimize a website for better performance and user experience?"
    
    print(f"Problem: {problem}")
    print("Approach: Comprehensive")
    print("\n🤖 Response:")
    response = runner.solve_problem(problem, "comprehensive", max_tokens=350)
    print(response)
    
    # Example 8: Text Summarization
    print("\n" + "="*60)
    print("Example 8: Text Summarization")
    print("="*60)
    
    long_text = """Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It involves algorithms that can identify patterns in data and make predictions or decisions based on those patterns. There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled training data to learn the relationship between inputs and outputs. Unsupervised learning finds hidden patterns in unlabeled data. Reinforcement learning learns through trial and error by receiving rewards or penalties for actions."""
    
    print(f"Text to summarize: {long_text[:100]}...")
    print("Length: Detailed")
    print("\n🤖 Response:")
    response = runner.summarize_text(long_text, "detailed", max_tokens=150)
    print(response)
    
    # Example 9: Brainstorming
    print("\n" + "="*60)
    print("Example 9: Brainstorming")
    print("="*60)
    
    print("Topic: Innovative ways to use AI in education")
    print("Number of ideas: 5")
    print("\n🤖 Response:")
    response = runner.brainstorm_ideas("innovative ways to use AI in education", 5, max_tokens=400)
    print(response)
    
    print("\n✅ All enhanced examples completed!")

def show_prompt_templates():
    """Show available prompt templates"""
    print("\n🎯 Available Prompt Templates:")
    print("=" * 40)
    
    templates = [
        ("General Question", "question <text>", "Ask structured questions"),
        ("Explanation", "explain <topic>", "Get detailed explanations"),
        ("Code Generation", "code <language> <task>", "Generate code with requirements"),
        ("Creative Writing", "write <genre> <topic>", "Create structured creative content"),
        ("Text Analysis", "analyze <text>", "Analyze text with different approaches"),
        ("Comparison", "compare <item1> vs <item2>", "Compare items systematically"),
        ("Problem Solving", "solve <problem>", "Solve problems with structured approach"),
        ("Summarization", "summarize <text>", "Summarize text at different levels"),
        ("Brainstorming", "brainstorm <topic>", "Generate creative ideas")
    ]
    
    for i, (name, usage, description) in enumerate(templates, 1):
        print(f"{i}. {name}")
        print(f"   Usage: {usage}")
        print(f"   Description: {description}")
        print()

if __name__ == "__main__":
    print("🤖 Enhanced Mistral 7B Prompt Examples")
    print("This demonstrates improved prompt templates for better responses")
    
    try:
        # Show available templates
        show_prompt_templates()
        
        # Run examples
        demonstrate_enhanced_prompts()
        
    except Exception as e:
        print(f"❌ Error running examples: {e}") 