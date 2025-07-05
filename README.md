# MistralAI Desktop - Local LLM Runner

🚀 **A powerful, memory-optimized desktop application for running Mistral 7B locally on resource-constrained systems**

A comprehensive Python application that brings the power of Mistral 7B language model to your desktop with multiple interfaces, enhanced prompts, and optimized performance for laptops with limited RAM.

## ✨ Key Features

- 🧠 **Memory Optimized**: Configured for 6GB RAM laptops with intelligent memory management
- 🌐 **Multiple Interfaces**: Command-line, interactive chat, REST API, and modern Web UI
- 🎯 **Enhanced Prompts**: 20+ intelligent prompt templates for various use cases
- 🔧 **Easy Setup**: One-command installation and configuration
- 📊 **Swagger API**: Interactive API documentation with testing interface
- 🎨 **Modern Web UI**: Beautiful, responsive chat interface with real-time features
- 📱 **Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- 🔒 **Privacy First**: All processing happens locally on your machine

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download Model

Place your Mistral 7B GGUF model in the `models/` directory:
```
models/
└── mistral-7b-v0.1.Q4_K_M.gguf
```

### 3. Run the Application

#### 🌐 Web UI (Recommended)
```bash
# Start both API server and web UI with one command
python start_web_ui.py
```

Then open your browser to: **http://localhost:8081**

#### 💻 Command Line
```bash
# Single query
python run_mistral.py "What is artificial intelligence?"

# Interactive chat
python run_mistral.py
```

#### 🎯 Enhanced Prompts
```bash
# Enhanced version with intelligent prompt templates
python simple_enhanced.py "What is artificial intelligence?"

# Interactive enhanced chat
python simple_enhanced.py
```

## 🎨 Web UI Features

The web interface provides a modern, responsive chat experience:

- **Beautiful Design**: Modern gradient UI with smooth animations
- **Real-time Chat**: Instant message exchange with typing indicators
- **Conversation History**: Persistent chat sessions
- **API Status**: Real-time connection status indicator
- **Mobile Responsive**: Works on desktop, tablet, and mobile
- **Auto-resize**: Smart textarea that grows with content
- **Clear Chat**: One-click conversation reset
- **Error Handling**: Graceful error messages and recovery

## 🎯 Enhanced Prompt System

The enhanced version includes 20+ intelligent prompt templates:

### Available Prompt Types

1. **Question**: `question <text>` - Ask simple questions
2. **Explanation**: `explain <topic>` - Explain topics simply
3. **Code Generation**: `code <language> <task>` - Generate code with comments
4. **Creative Writing**: `write <genre> <topic>` - Write creative content
5. **Text Analysis**: `analyze <text>` - Analyze text
6. **Comparison**: `compare <item1> vs <item2>` - Compare items
7. **Problem Solving**: `solve <problem>` - Solve problems
8. **Summarization**: `summarize <text>` - Summarize text
9. **Brainstorming**: `brainstorm <topic>` - Generate creative ideas
10. **Definition**: `define <term>` - Get definitions
11. **Example**: `example <concept>` - Get examples
12. **Tips**: `tips <topic>` - Get tips
13. **Pros/Cons**: `pros_cons <topic>` - Get pros and cons
14. **How-to**: `how_to <task>` - Get how-to instructions
15. **Fact Check**: `fact_check <statement>` - Check if statement is true
16. **Step-by-step**: `step_by_step <instruction>` - Follow instructions
17. **List Items**: `list_items <category> <count>` - List items
18. **Why**: `why <question>` - Ask why
19. **What-if**: `what_if <scenario>` - Ask what-if
20. **Best Practice**: `best_practice <topic>` - Get best practices
21. **Common Mistakes**: `common_mistakes <topic>` - Get common mistakes

## 🔌 API Usage

### Start the Server
```bash
python api_server.py
```

### Generate Text
```bash
curl -X POST "http://localhost:5000/generate" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "What is artificial intelligence?",
       "max_tokens": 200,
       "temperature": 0.2
     }'
```

### Health Check
```bash
curl http://localhost:5000/health
```

### Swagger Documentation
Visit `http://localhost:5000/` for interactive API documentation.

## 📁 Project Structure

```
MistralAI Desktop/
├── api_server.py          # Flask REST API server
├── web_ui.py              # Flask web interface
├── start_web_ui.py        # Startup script for web UI
├── run_mistral.py         # Basic Mistral runner
├── simple_enhanced.py     # Enhanced runner with prompt templates
├── simple_prompts.py      # Simple, effective prompt templates
├── prompt_templates.py    # Comprehensive prompt templates
├── test_api.py            # API test client
├── prompt_examples.py     # Examples of all prompt types
├── requirements.txt       # Python dependencies
├── templates/
│   └── chat.html          # Web UI template
├── models/
│   └── README.md          # Model installation instructions
└── llama.cpp/             # Git submodule for llama.cpp
```

## ⚡ Memory Optimization

The application is specifically configured for 6GB RAM laptops:

- **Context Window**: 2048 tokens (reduced from default)
- **Batch Size**: 512 (smaller batches)
- **GPU Layers**: 0 (CPU only)
- **Memory Mapping**: Enabled
- **Memory Locking**: Disabled (allows swapping)

## 🎯 Example Usage

### Basic Questions
```bash
python simple_enhanced.py "What is the capital of France?"
```

### Code Generation
```bash
python simple_enhanced.py "code Python create a web scraper"
```

### Creative Writing
```bash
python simple_enhanced.py "write fantasy story about dragons"
```

### Problem Solving
```bash
python simple_enhanced.py "solve how to optimize database queries"
```

## 🔧 Troubleshooting

### Model Not Responding
- Ensure the model file exists in `models/` directory
- Check available RAM (minimum 4GB recommended)
- Try reducing `max_tokens` parameter

### API Connection Issues
- Verify the server is running on port 5000
- Check firewall settings
- Ensure all dependencies are installed

### Web UI Issues
- Make sure both API server and web UI are running
- Check browser console for JavaScript errors
- Verify ports 5000 and 8081 are not in use

### Memory Issues
- Close other applications to free RAM
- Reduce `n_ctx` (context window) in the code
- Use CPU-only mode (already configured)

## 📋 Requirements

- Python 3.8+
- 6GB RAM (minimum 4GB)
- Mistral 7B GGUF model file
- Linux/macOS/Windows

## 📦 Dependencies

- llama-cpp-python
- Flask
- Flask-RESTX
- requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is for educational purposes. Please respect the Mistral model's license terms.

## 🙏 Acknowledgments

- [llama.cpp](https://github.com/ggerganov/llama.cpp) - The underlying inference engine
- [Mistral AI](https://mistral.ai/) - For the amazing Mistral 7B model
- [TheBloke](https://huggingface.co/TheBloke) - For providing GGUF model conversions