#!/usr/bin/env python3
"""
Test client for Mistral 7B API
Demonstrates how to use the API endpoints
"""

import requests
import json
import time

API_BASE = "http://localhost:5000"

def test_health():
    """Test the health endpoint"""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE}/mistral/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_generate(prompt, max_tokens=100, temperature=0.2):
    """Test the generate endpoint"""
    print(f"\n🤖 Testing generate endpoint...")
    print(f"Prompt: {prompt}")
    
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        response = requests.post(
            f"{API_BASE}/mistral/generate",
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"Status: {response.status_code}")
        result = response.json()
        
        if result.get('success'):
            print(f"✅ Response: {result['response']}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
        
        return result.get('success', False)
        
    except Exception as e:
        print(f"❌ Generate request failed: {e}")
        return False

def main():
    print("🧪 Mistral 7B API Test Client")
    print("=" * 50)
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(5)
    
    # Test health
    if not test_health():
        print("❌ Server not ready. Make sure to start the API server first:")
        print("   python api_server.py")
        return
    
    # Test different types of prompts
    test_cases = [
        ("What is the capital of France?", 50, 0.2),
        ("Write a short poem about AI", 100, 0.8),
        ("Explain quantum computing", 150, 0.5),
        ("Write a Python function to calculate fibonacci", 120, 0.3)
    ]
    
    for prompt, max_tokens, temperature in test_cases:
        test_generate(prompt, max_tokens, temperature)
        time.sleep(1)  # Small delay between requests
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main() 