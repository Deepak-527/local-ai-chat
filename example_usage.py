#!/usr/bin/env python3
"""
Example usage of the Mistral 7B model
Demonstrates different ways to interact with the model
"""

from run_mistral import MistralRunner

def example_queries():
    """Run some example queries to demonstrate the model's capabilities"""
    
    # Initialize the model
    print("🚀 Initializing Mistral model...")
    runner = MistralRunner()
    
    # Example 1: Simple question
    print("\n" + "="*50)
    print("Example 1: Simple Question")
    print("="*50)
    query1 = "What is the capital of France?"
    print(f"Query: {query1}")
    response1 = runner.generate_response(query1, max_tokens=100)
    print(f"Response: {response1}")
    
    # Example 2: Creative writing
    print("\n" + "="*50)
    print("Example 2: Creative Writing")
    print("="*50)
    query2 = "Write a short story about a robot learning to paint"
    print(f"Query: {query2}")
    response2 = runner.generate_response(query2, max_tokens=200, temperature=0.8)
    print(f"Response: {response2}")
    
    # Example 3: Code generation
    print("\n" + "="*50)
    print("Example 3: Code Generation")
    print("="*50)
    query3 = "Write a Python function to calculate the factorial of a number"
    print(f"Query: {query3}")
    response3 = runner.generate_response(query3, max_tokens=150, temperature=0.3)
    print(f"Response: {response3}")
    
    # Example 4: Explanation
    print("\n" + "="*50)
    print("Example 4: Explanation")
    print("="*50)
    query4 = "Explain quantum computing in simple terms"
    print(f"Query: {query4}")
    response4 = runner.generate_response(query4, max_tokens=250, temperature=0.5)
    print(f"Response: {response4}")

def custom_prompt_example():
    """Example of using custom prompts with different parameters"""
    
    print("\n" + "="*50)
    print("Custom Prompt Examples")
    print("="*50)
    
    runner = MistralRunner()
    
    # High creativity (high temperature)
    print("\n🎨 High Creativity Example:")
    prompt1 = "Create a poem about artificial intelligence"
    response1 = runner.generate_response(prompt1, max_tokens=150, temperature=0.9)
    print(f"Prompt: {prompt1}")
    print(f"Response: {response1}")
    
    # Low creativity (low temperature) - more deterministic
    print("\n📚 Factual Example:")
    prompt2 = "List the main components of a computer"
    response2 = runner.generate_response(prompt2, max_tokens=100, temperature=0.1)
    print(f"Prompt: {prompt2}")
    print(f"Response: {response2}")

if __name__ == "__main__":
    print("🤖 Mistral 7B Example Usage")
    print("This script demonstrates various ways to use the model")
    
    try:
        # Run example queries
        example_queries()
        
        # Run custom prompt examples
        custom_prompt_example()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}") 