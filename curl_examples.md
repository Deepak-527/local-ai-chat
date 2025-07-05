# Mistral 7B API - cURL Examples

## Prerequisites
1. Start the API server: `python api_server.py`
2. Wait for the model to load (check health endpoint)

## Base URL
```
http://localhost:5000
```

## Endpoints

### 1. Health Check
Check if the API and model are ready.

```bash
curl -X GET "http://localhost:5000/mistral/health"
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "uptime": "0h 2m 15s"
}
```

### 2. Generate Text
Generate text using the Mistral model.

```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "What is the capital of France?",
    "max_tokens": 100,
    "temperature": 0.2
  }'
```

**Response:**
```json
{
  "success": true,
  "response": "Paris. Paris is the capital and largest city in France...",
  "error": null
}
```

### 3. Creative Writing
Generate creative content with higher temperature.

```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a short poem about artificial intelligence",
    "max_tokens": 150,
    "temperature": 0.8
  }'
```

### 4. Code Generation
Generate code with lower temperature for consistency.

```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a Python function to calculate fibonacci numbers",
    "max_tokens": 200,
    "temperature": 0.3
  }'
```

### 5. Explanation
Get detailed explanations.

```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain quantum computing in simple terms",
    "max_tokens": 300,
    "temperature": 0.5
  }'
```

## Error Handling

### Model Still Loading
```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello"}'
```

**Response:**
```json
{
  "success": false,
  "response": "",
  "error": "Model loading..."
}
```

### Invalid Request
```bash
curl -X POST "http://localhost:5000/mistral/generate" \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Response:**
```json
{
  "success": false,
  "response": "",
  "error": "Prompt required"
}
```

## Python Examples

### Using requests library
```python
import requests

# Generate text
response = requests.post(
    "http://localhost:5000/mistral/generate",
    json={
        "prompt": "What is the capital of France?",
        "max_tokens": 100,
        "temperature": 0.2
    }
)

if response.json()["success"]:
    print(response.json()["response"])
else:
    print("Error:", response.json()["error"])
```

### Using test_api.py
```bash
python test_api.py
```

## Swagger Documentation
Visit `http://localhost:5000/docs` for interactive API documentation. 