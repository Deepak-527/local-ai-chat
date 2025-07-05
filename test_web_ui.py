#!/usr/bin/env python3
"""
Test script for KickGPT Web UI
Tests the web UI endpoints and functionality
"""

import requests
import time
import json

def test_web_ui():
    """Test the web UI functionality"""
    base_url = "http://localhost:8081"
    
    print("🧪 Testing KickGPT Web UI")
    print("=" * 40)
    
    # Test 1: Check if web UI is running
    print("1. Testing web UI availability...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Web UI is running")
        else:
            print(f"❌ Web UI returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Web UI is not running. Start it with: python web_ui.py")
        return False
    except Exception as e:
        print(f"❌ Error connecting to web UI: {e}")
        return False
    
    # Test 2: Check API status endpoint
    print("\n2. Testing API status endpoint...")
    try:
        response = requests.get(f"{base_url}/api/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Status: {data}")
        else:
            print(f"❌ API status endpoint returned: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing API status: {e}")
    
    # Test 3: Test conversation endpoint
    print("\n3. Testing conversation endpoint...")
    try:
        response = requests.get(f"{base_url}/api/conversation", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Conversation loaded: {len(data.get('conversation', []))} messages")
        else:
            print(f"❌ Conversation endpoint returned: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing conversation: {e}")
    
    # Test 4: Test chat endpoint
    print("\n4. Testing chat endpoint...")
    try:
        test_message = "Hello! This is a test message."
        response = requests.post(
            f"{base_url}/api/chat",
            json={"message": test_message},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Chat endpoint working")
            print(f"📝 Response length: {len(data.get('response', ''))} characters")
        elif response.status_code == 503:
            print("⚠️  Chat endpoint working but API server not running")
            print("💡 Start the API server with: python api_server.py")
        else:
            print(f"❌ Chat endpoint returned: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.Timeout:
        print("⚠️  Chat request timed out (this is normal for first request)")
    except Exception as e:
        print(f"❌ Error testing chat: {e}")
    
    # Test 5: Test clear conversation
    print("\n5. Testing clear conversation...")
    try:
        response = requests.post(f"{base_url}/api/clear", timeout=5)
        if response.status_code == 200:
            print("✅ Clear conversation working")
        else:
            print(f"❌ Clear conversation returned: {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing clear: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 Web UI testing completed!")
    print("\n📋 Summary:")
    print("- Web UI: http://localhost:8081")
    print("- API Server: http://localhost:5000")
    print("- API Docs: http://localhost:5000/")
    print("\n💡 To start everything:")
    print("python start_web_ui.py")
    
    return True

def check_services():
    """Check if required services are running"""
    print("🔍 Checking service status...")
    
    # Check API server
    try:
        response = requests.get("http://localhost:5000/mistral/health", timeout=5)
        if response.status_code == 200:
            print("✅ API Server: Running (port 5000)")
        else:
            print("❌ API Server: Not responding properly")
    except:
        print("❌ API Server: Not running (port 5000)")
    
    # Check web UI
    try:
        response = requests.get("http://localhost:8081/", timeout=5)
        if response.status_code == 200:
            print("✅ Web UI: Running (port 8081)")
        else:
            print("❌ Web UI: Not responding properly")
    except:
        print("❌ Web UI: Not running (port 8081)")

if __name__ == "__main__":
    print("🚀 KickGPT Web UI Test")
    print("=" * 50)
    
    # Check services first
    check_services()
    print()
    
    # Run tests
    test_web_ui() 