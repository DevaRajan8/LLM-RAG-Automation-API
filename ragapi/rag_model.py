import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Define the automation functions metadata.
FUNCTIONS = [
    {"name": "open_chrome", "description": "Open Google Chrome by navigating to Google."},
    {"name": "open_calculator", "description": "Open the calculator application on Windows."},
    {"name": "open_notepad", "description": "Open Notepad application on Windows."},
    {"name": "cpu_usage", "description": "Retrieve the current CPU usage percentage."},
    {"name": "ram_usage", "description": "Retrieve the current RAM usage percentage."},
    {"name": "run_shell_command", "description": "Execute a shell command and return its output."}
]

# Initialize the embedding model.
MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

# Pre-compute embeddings for each function description.
function_descriptions = [f["description"] for f in FUNCTIONS]
embeddings = model.encode(function_descriptions, convert_to_numpy=True)

# Create a FAISS index. For small datasets, IndexFlatL2 is sufficient.
d = embeddings.shape[1]  # embedding dimensionality
index = faiss.IndexFlatL2(d)
index.add(embeddings)

def retrieve_function(query, top_k=1):
    """
    Retrieves the best-matching function name from the registry based on the query.
    Uses SentenceTransformers for embedding and FAISS for nearest neighbor search.
    """
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    
    # Get the function with the smallest distance.
    best_index = indices[0][0]
    return FUNCTIONS[best_index]["name"]
