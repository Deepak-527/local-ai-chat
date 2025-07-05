#!/usr/bin/env python3
"""
KickGPT Quick Start Guide
Shows all available options and helps users get started
"""

import os
import sys
import subprocess
from pathlib import Path

def check_model():
    """Check if model file exists"""
    model_path = Path("models/mistral-7b-v0.1.Q4_K_M.gguf")
    if model_path.exists():
        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"✅ Model found: {model_path.name} ({size_mb:.1f} MB)")
        return True
    else:
        print(f"❌ Model not found: {model_path}")
        print("Please download the Mistral 7B GGUF model to the models/ directory")
        return False

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
        print(f"❌ Missing dependencies: {', '.join(missing_packages)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed")
    return True

def show_menu():
    """Show the main menu"""
    print("\n🚀 KickGPT - Quick Start Menu")
    print("=" * 50)
    print("Choose how you want to interact with Mistral 7B:")
    print()
    print("1. 🌐 Web UI (RECOMMENDED)")
    print("   Beautiful web interface with real-time chat")
    print("   Access: http://localhost:8081")
    print()
    print("2. 💻 Command Line - Enhanced")
    print("   Interactive chat with 20+ prompt templates")
    print("   Best for: Development, testing, automation")
    print()
    print("3. 🌐 REST API")
    print("   HTTP API with Swagger documentation")
    print("   Best for: Integration, mobile apps, scripts")
    print()
    print("4. 💻 Command Line - Basic")
    print("   Simple command-line interface")
    print("   Best for: Quick queries, scripting")
    print()
    print("5. 🎮 Interactive Demo")
    print("   Try all features interactively")
    print("   Best for: Exploring capabilities")
    print()
    print("6. 🧪 Test Everything")
    print("   Run tests to verify everything works")
    print("   Best for: Troubleshooting")
    print()
    print("7. 📚 View Documentation")
    print("   Show README and examples")
    print("   Best for: Learning more")
    print()
    print("0. ❌ Exit")

def run_web_ui():
    """Start the web UI"""
    print("\n🌐 Starting Web UI...")
    print("This will start both the API server and web interface")
    
    try:
        subprocess.run([sys.executable, "start_web_ui.py"])
    except KeyboardInterrupt:
        print("\n👋 Web UI stopped")
    except Exception as e:
        print(f"❌ Error starting web UI: {e}")

def run_enhanced_cli():
    """Start enhanced command line interface"""
    print("\n💻 Starting Enhanced CLI...")
    print("Type 'help' for available commands")
    
    try:
        subprocess.run([sys.executable, "simple_enhanced.py"])
    except KeyboardInterrupt:
        print("\n👋 CLI stopped")
    except Exception as e:
        print(f"❌ Error starting CLI: {e}")

def run_api_server():
    """Start the API server"""
    print("\n🌐 Starting API Server...")
    print("API will be available at: http://localhost:5000")
    print("Swagger docs at: http://localhost:5000/")
    
    try:
        subprocess.run([sys.executable, "api_server.py"])
    except KeyboardInterrupt:
        print("\n👋 API server stopped")
    except Exception as e:
        print(f"❌ Error starting API server: {e}")

def run_basic_cli():
    """Start basic command line interface"""
    print("\n💻 Starting Basic CLI...")
    
    try:
        subprocess.run([sys.executable, "run_mistral.py"])
    except KeyboardInterrupt:
        print("\n👋 CLI stopped")
    except Exception as e:
        print(f"❌ Error starting CLI: {e}")

def run_demo():
    """Run the interactive demo"""
    print("\n🎮 Starting Interactive Demo...")
    
    try:
        subprocess.run([sys.executable, "demo.py"])
    except KeyboardInterrupt:
        print("\n👋 Demo stopped")
    except Exception as e:
        print(f"❌ Error starting demo: {e}")

def run_tests():
    """Run tests"""
    print("\n🧪 Running Tests...")
    
    # Test web UI
    print("\n1. Testing Web UI...")
    try:
        subprocess.run([sys.executable, "test_web_ui.py"])
    except Exception as e:
        print(f"❌ Web UI test failed: {e}")
    
    # Test API
    print("\n2. Testing API...")
    try:
        subprocess.run([sys.executable, "test_api.py"])
    except Exception as e:
        print(f"❌ API test failed: {e}")

def show_documentation():
    """Show documentation"""
    print("\n📚 Documentation")
    print("=" * 30)
    
    docs = [
        ("README.md", "Main documentation"),
        ("curl_examples.md", "API usage examples"),
        ("prompt_examples.py", "Prompt template examples"),
        ("enhanced_examples.py", "Enhanced prompt examples")
    ]
    
    for filename, description in docs:
        if os.path.exists(filename):
            print(f"✅ {filename} - {description}")
        else:
            print(f"❌ {filename} - {description} (not found)")
    
    print("\n💡 Quick Commands:")
    print("- python start_web_ui.py    # Start web UI")
    print("- python simple_enhanced.py # Enhanced CLI")
    print("- python api_server.py      # API server")
    print("- python demo.py            # Interactive demo")

def main():
    """Main function"""
    print("🚀 Welcome to KickGPT!")
    print("Local Mistral 7B Chat System")
    print("=" * 50)
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    model_ok = check_model()
    deps_ok = check_dependencies()
    
    if not model_ok or not deps_ok:
        print("\n❌ Please fix the issues above before continuing")
        return
    
    print("\n✅ All prerequisites met!")
    
    while True:
        show_menu()
        
        try:
            choice = input("\n🎯 Select option (0-7): ").strip()
            
            if choice == "0":
                print("👋 Thanks for using KickGPT!")
                break
            elif choice == "1":
                run_web_ui()
            elif choice == "2":
                run_enhanced_cli()
            elif choice == "3":
                run_api_server()
            elif choice == "4":
                run_basic_cli()
            elif choice == "5":
                run_demo()
            elif choice == "6":
                run_tests()
            elif choice == "7":
                show_documentation()
            else:
                print("❌ Invalid choice. Please select 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 