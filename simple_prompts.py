#!/usr/bin/env python3
"""
Simple and Effective Prompt Templates for Mistral 7B
Optimized for better responses with minimal prompt overhead
"""

class SimplePrompts:
    """Simple prompt templates that work well with Mistral 7B"""
    
    @staticmethod
    def question(q: str) -> str:
        """Simple question format"""
        return f"Answer this question: {q}"
    
    @staticmethod
    def explain(topic: str) -> str:
        """Simple explanation format"""
        return f"Explain {topic} in simple terms."
    
    @staticmethod
    def code(language: str, task: str) -> str:
        """Simple code generation format"""
        return f"Write {language} code to {task}. Include comments."
    
    @staticmethod
    def write(genre: str, topic: str) -> str:
        """Simple creative writing format"""
        return f"Write a {genre} story about {topic}."
    
    @staticmethod
    def analyze(text: str) -> str:
        """Simple analysis format"""
        return f"Analyze this text: {text}"
    
    @staticmethod
    def compare(item1: str, item2: str) -> str:
        """Simple comparison format"""
        return f"Compare {item1} and {item2}."
    
    @staticmethod
    def solve(problem: str) -> str:
        """Simple problem solving format"""
        return f"Solve this problem: {problem}"
    
    @staticmethod
    def summarize(text: str) -> str:
        """Simple summarization format"""
        return f"Summarize this: {text}"
    
    @staticmethod
    def brainstorm(topic: str) -> str:
        """Simple brainstorming format"""
        return f"Give me 5 creative ideas about {topic}."
    
    @staticmethod
    def step_by_step(instruction: str) -> str:
        """Step-by-step instruction format"""
        return f"Follow these steps: {instruction}"
    
    @staticmethod
    def fact_check(statement: str) -> str:
        """Fact checking format"""
        return f"Is this true? {statement}"
    
    @staticmethod
    def pros_cons(topic: str) -> str:
        """Pros and cons format"""
        return f"What are the pros and cons of {topic}?"
    
    @staticmethod
    def how_to(task: str) -> str:
        """How-to format"""
        return f"How to {task}?"
    
    @staticmethod
    def definition(term: str) -> str:
        """Definition format"""
        return f"What is {term}?"
    
    @staticmethod
    def example(concept: str) -> str:
        """Example format"""
        return f"Give me an example of {concept}."
    
    @staticmethod
    def list_items(category: str, count: int = 5) -> str:
        """List format"""
        return f"List {count} {category}."
    
    @staticmethod
    def why(question: str) -> str:
        """Why format"""
        return f"Why {question}?"
    
    @staticmethod
    def what_if(scenario: str) -> str:
        """What-if format"""
        return f"What if {scenario}?"
    
    @staticmethod
    def best_practice(topic: str) -> str:
        """Best practices format"""
        return f"What are the best practices for {topic}?"
    
    @staticmethod
    def common_mistakes(topic: str) -> str:
        """Common mistakes format"""
        return f"What are common mistakes when {topic}?"
    
    @staticmethod
    def tips(topic: str) -> str:
        """Tips format"""
        return f"Give me tips for {topic}."

# Quick access functions
def q(text: str) -> str:
    """Quick question"""
    return SimplePrompts.question(text)

def e(topic: str) -> str:
    """Quick explanation"""
    return SimplePrompts.explain(topic)

def c(language: str, task: str) -> str:
    """Quick code generation"""
    return SimplePrompts.code(language, task)

def w(genre: str, topic: str) -> str:
    """Quick writing"""
    return SimplePrompts.write(genre, topic)

def a(text: str) -> str:
    """Quick analysis"""
    return SimplePrompts.analyze(text)

def comp(item1: str, item2: str) -> str:
    """Quick comparison"""
    return SimplePrompts.compare(item1, item2)

def s(problem: str) -> str:
    """Quick problem solving"""
    return SimplePrompts.solve(problem)

def sum(text: str) -> str:
    """Quick summarization"""
    return SimplePrompts.summarize(text)

def b(topic: str) -> str:
    """Quick brainstorming"""
    return SimplePrompts.brainstorm(topic) 