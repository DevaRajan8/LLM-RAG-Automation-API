from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_model import retrieve_function
from code_generator import generate_code

app = FastAPI()

class ExecuteRequest(BaseModel):
    prompt: str

@app.post("/execute")
async def execute(request: ExecuteRequest):
    prompt = request.prompt
    func_name = retrieve_function(prompt)
    if not func_name:
        raise HTTPException(status_code=404, detail="No matching function found for the given prompt.")
    code = generate_code(func_name)
    return {"function": func_name, "code": code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
