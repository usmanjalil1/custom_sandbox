from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import subprocess
import os 

app = FastAPI(title = "Custom Sandbox Service", version = "0.1", description = "A custom sandbox service for running shell commands, Python code, and installing/uninstalling dependencies.", docs_url="/_docs")

UPLOAD_DIR = "/sandbox_env"  

os.makedirs(UPLOAD_DIR, exist_ok=True)


# Request models
class CommandRequest(BaseModel):
    command: str

class PythonCodeRequest(BaseModel):
    code: str

class PackageRequest(BaseModel):
    package: str

# Run shell command
@app.post("/run-command/")
async def run_command(request: CommandRequest):
    result = subprocess.run(request.command, shell=True, capture_output=True, text=True)
    return {"stdout": result.stdout, "stderr": result.stderr}

# Run Python code
@app.post("/run-python/")
async def run_python(request: PythonCodeRequest):
    try:
        result = subprocess.run(["python3", "-c", request.code], text=True, capture_output=True)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Install dependency
@app.post("/install-dependency/")
async def install_dependency(request: PackageRequest):
    result = subprocess.run(f"pip install {request.package}", shell=True, capture_output=True, text=True)
    return {"stdout": result.stdout, "stderr": result.stderr}

# Uninstall dependency
@app.post("/uninstall-dependency/")
async def uninstall_dependency(request: PackageRequest):
    result = subprocess.run(f"pip uninstall -y {request.package}", shell=True, capture_output=True, text=True)
    return {"stdout": result.stdout, "stderr": result.stderr}

# Upload file
@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename, "location": file_location}