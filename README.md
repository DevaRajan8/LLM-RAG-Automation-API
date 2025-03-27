# LLM + RAG-Based Function Execution API

## Overview

This project demonstrates an API service that dynamically retrieves and executes automation functions using a real RAG (Retrieval-Augmented Generation) approach. It uses SentenceTransformers to convert user queries into embeddings, FAISS for vector similarity search, and FastAPI to expose a REST endpoint.

## Repository Structure

```
project/
│── automation_functions.py   # Contains the function registry
│── rag_model.py              # Implements RAG using SentenceTransformers and FAISS
│── code_generator.py         # Generates dynamic function invocation code
│── api.py                    # FastAPI REST API service
```

## Contributing

If you wish to edit or improve this repository, please **fork** it. Once you have made your changes, submit a **pull request**. This ensures that all contributions are reviewed before being merged into the main branch.

## Setup and Running

### 1. Install Dependencies
Use pip to install all required packages:
```bash
pip install -r requirements.txt
```

### 2. Run the API Server
Start the server with:
```bash
python api.py
```
The server will be running at [http://localhost:8000](http://localhost:8000).

### 3. Test the Endpoint
Use `curl` or **Postman** to test the API:
```bash
curl -X POST "http://localhost:8000/execute" -H "Content-Type: application/json" -d '{"prompt": "Open Calculator"}'
```

### 4. Sample Outputs :
Prompts :
```bash
'{"prompt": "Open Calculator"}'
```

![Screenshot 2025-03-27 094205](https://github.com/user-attachments/assets/2bec4bb9-029e-4266-9fd7-f835427afbb0)

