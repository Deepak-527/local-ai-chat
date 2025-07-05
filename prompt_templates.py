#!/usr/bin/env python3
"""
Prompt Templates for Mistral 7B
Provides structured prompts for different types of tasks
"""

class PromptTemplates:
    """Collection of prompt templates for different use cases"""
    
    @staticmethod
    def general_question(question: str, context: str = "") -> str:
        """Template for general questions"""
        if context:
            return f"""Context: {context}

Question: {question}

Please provide a clear, accurate, and helpful answer."""
        else:
            return f"""Question: {question}

Please provide a clear, accurate, and helpful answer."""
    
    @staticmethod
    def explanation(topic: str, level: str = "simple") -> str:
        """Template for explanations"""
        level_instructions = {
            "simple": "Explain in simple terms that anyone can understand",
            "detailed": "Provide a comprehensive explanation with examples",
            "technical": "Give a technical explanation with specific details"
        }
        
        return f"""Please {level_instructions.get(level, level_instructions["simple"])} about: {topic}

Structure your response with:
1. Brief overview
2. Key points
3. Examples (if applicable)
4. Summary"""
    
    @staticmethod
    def code_generation(language: str, task: str, requirements: str = "") -> str:
        """Template for code generation"""
        req_text = f"\nRequirements: {requirements}" if requirements else ""
        
        return f"""Write {language} code to {task}.{req_text}

Please provide:
1. Clean, well-commented code
2. Brief explanation of the approach
3. Example usage (if applicable)

Focus on readability and best practices."""
    
    @staticmethod
    def creative_writing(genre: str, topic: str, length: str = "short") -> str:
        """Template for creative writing"""
        length_guide = {
            "short": "Write a brief piece (2-3 paragraphs)",
            "medium": "Write a medium-length piece (4-6 paragraphs)", 
            "long": "Write a longer piece (8-10 paragraphs)"
        }
        
        return f"""Write a {genre} piece about: {topic}

{length_guide.get(length, length_guide["short"])}

Make it engaging, creative, and well-structured."""
    
    @staticmethod
    def analysis(text: str, analysis_type: str = "general") -> str:
        """Template for text analysis"""
        analysis_instructions = {
            "general": "Provide a general analysis of the main points and themes",
            "critical": "Provide a critical analysis examining strengths and weaknesses",
            "sentiment": "Analyze the sentiment and emotional tone",
            "technical": "Provide a technical analysis of the content structure"
        }
        
        return f"""Analyze the following text:

"{text}"

{analysis_instructions.get(analysis_type, analysis_instructions["general"])}

Structure your analysis with:
1. Main points
2. Key insights
3. Conclusion"""
    
    @staticmethod
    def comparison(item1: str, item2: str, criteria: str = "") -> str:
        """Template for comparisons"""
        criteria_text = f"\nCompare based on: {criteria}" if criteria else ""
        
        return f"""Compare {item1} and {item2}.{criteria_text}

Provide a structured comparison with:
1. Similarities
2. Differences
3. Key advantages of each
4. Overall recommendation (if applicable)"""
    
    @staticmethod
    def problem_solving(problem: str, approach: str = "step-by-step") -> str:
        """Template for problem solving"""
        approach_instructions = {
            "step-by-step": "Break down the solution into clear steps",
            "creative": "Think outside the box and provide innovative solutions",
            "practical": "Focus on practical, implementable solutions",
            "comprehensive": "Provide multiple approaches and considerations"
        }
        
        return f"""Problem: {problem}

{approach_instructions.get(approach, approach_instructions["step-by-step"])}

Structure your response with:
1. Problem understanding
2. Solution approach
3. Implementation steps
4. Potential challenges and solutions"""
    
    @staticmethod
    def summarization(text: str, length: str = "brief") -> str:
        """Template for summarization"""
        length_guide = {
            "brief": "Provide a concise summary (1-2 sentences)",
            "detailed": "Provide a detailed summary (3-4 sentences)",
            "comprehensive": "Provide a comprehensive summary (5-6 sentences)"
        }
        
        return f"""Summarize the following text:

"{text}"

{length_guide.get(length, length_guide["brief"])}

Focus on the key points and main ideas."""
    
    @staticmethod
    def instruction_following(instruction: str, context: str = "") -> str:
        """Template for following specific instructions"""
        context_text = f"\nContext: {context}" if context else ""
        
        return f"""Instruction: {instruction}{context_text}

Please follow the instruction precisely and provide a complete response."""
    
    @staticmethod
    def brainstorming(topic: str, num_ideas: int = 5) -> str:
        """Template for brainstorming"""
        return f"""Brainstorm {num_ideas} creative ideas about: {topic}

For each idea, provide:
1. Brief description
2. Key benefits
3. Potential challenges

Think creatively and consider different perspectives."""

# Example usage function
def get_prompt(prompt_type: str, **kwargs) -> str:
    """
    Get a formatted prompt based on type and parameters
    
    Args:
        prompt_type: Type of prompt (e.g., 'general_question', 'explanation', etc.)
        **kwargs: Parameters for the specific prompt type
    
    Returns:
        Formatted prompt string
    """
    templates = PromptTemplates()
    
    if hasattr(templates, prompt_type):
        method = getattr(templates, prompt_type)
        return method(**kwargs)
    else:
        # Fallback to general question
        return PromptTemplates.general_question(kwargs.get('question', 'Hello'))

# Quick access functions
def question(q: str, context: str = "") -> str:
    """Quick function for general questions"""
    return PromptTemplates.general_question(q, context)

def explain(topic: str, level: str = "simple") -> str:
    """Quick function for explanations"""
    return PromptTemplates.explanation(topic, level)

def code(language: str, task: str, requirements: str = "") -> str:
    """Quick function for code generation"""
    return PromptTemplates.code_generation(language, task, requirements)

def write(genre: str, topic: str, length: str = "short") -> str:
    """Quick function for creative writing"""
    return PromptTemplates.creative_writing(genre, topic, length) 