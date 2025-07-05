#!/usr/bin/env python3
"""
KickGPT Web UI Startup Script
Launches both the API server and web UI
"""

import subprocess
import sys
import time
import os
import signal
import threading
from pathlib import Path

def check_model_exists():
    """Check if the Mistral model file exists"""
    model_path = Path("models/mistral-7b-v0.1.Q4_K_M.gguf")
    if not model_path.exists():
        print("❌ Model file not found!")
        print(f"Expected location: {model_path.absolute()}")
        print("Please ensure the Mistral 7B model file is in the models/ directory")
        return False
    return True

def start_api_server():
    """Start the API server"""
    print("🚀 Starting API Server...")
    try:
        process = subprocess.Popen([
            sys.executable, "api_server.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Wait a bit for the server to start
        time.sleep(3)
        
        if process.poll() is None:
            print("✅ API Server started successfully")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ API Server failed to start:")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
    except Exception as e:
        print(f"❌ Error starting API server: {e}")
        return None

def start_web_ui():
    """Start the web UI"""
    print("🌐 Starting Web UI...")
    try:
        process = subprocess.Popen([
            sys.executable, "web_ui.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Wait a bit for the server to start
        time.sleep(2)
        
        if process.poll() is None:
            print("✅ Web UI started successfully")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Web UI failed to start:")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
    except Exception as e:
        print(f"❌ Error starting Web UI: {e}")
        return None

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        ('llama_cpp', 'llama-cpp-python'),
        ('flask', 'flask'),
        ('requests', 'requests')
    ]
    missing_packages = []
    
    for import_name, package_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nInstall them with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def main():
    """Main startup function"""
    print("🚀 KickGPT Web UI Startup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check model file
    if not check_model_exists():
        return
    
    print("\n📋 Starting services...")
    
    # Start API server
    api_process = start_api_server()
    if not api_process:
        print("❌ Failed to start API server. Exiting.")
        return
    
    # Start web UI
    web_process = start_web_ui()
    if not web_process:
        print("❌ Failed to start Web UI. Stopping API server.")
        api_process.terminate()
        return
    
    print("\n🎉 Both services started successfully!")
    print("=" * 50)
    print("📡 API Server: http://localhost:5000")
    print("🌐 Web UI: http://localhost:8081")
    print("📚 API Docs: http://localhost:5000/docs")
    print("=" * 50)
    print("💡 Press Ctrl+C to stop both services")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
            
            # Check if processes are still running
            if api_process.poll() is not None:
                print("❌ API Server stopped unexpectedly")
                break
                
            if web_process.poll() is not None:
                print("❌ Web UI stopped unexpectedly")
                break
                
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down services...")
        
        # Terminate processes
        if api_process:
            api_process.terminate()
            print("✅ API Server stopped")
            
        if web_process:
            web_process.terminate()
            print("✅ Web UI stopped")
            
        print("👋 Goodbye!")

if __name__ == "__main__":
    main() 