## RUN SERVICE 

### Build & Run Docker Container

```
docker compose up --build -d
```

### Install `Sandox-env` Package

```
pip install ./sandbox_env
```

### Test Environment

```
from sandbox_env.client import SandboxClient

sandbox = SandboxClient(host="localhost")

# Run a shell command
print(sandbox.run_command("ls"))

# Run Python code
print(sandbox.run_python("print('Hello, Sandbox!')"))

# Upload a file
print(sandbox.upload_file("test.txt"))

# Install a dependency
print(sandbox.install_dependency("numpy"))

# Uninstall a dependency
print(sandbox.uninstall_dependency("numpy"))
```