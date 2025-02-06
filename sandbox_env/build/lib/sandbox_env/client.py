import requests

class SandboxClient:
    def __init__(self, host="sandbox_container", port=8000):
        self.base_url = f"http://{host}:{port}"

    def run_command(self, command):
        response = requests.post(f"{self.base_url}/run-command/", json={"command": command})
        return response.json()

    def run_python(self, code):
        response = requests.post(f"{self.base_url}/run-python/", json={"code": code})
        return response.json()

    def upload_file(self, filepath):
        with open(filepath, "rb") as file:
            files = {"file": file}
            response = requests.post(f"{self.base_url}/upload-file/", files=files)
        return response.json()

    def install_dependency(self, package):
        response = requests.post(f"{self.base_url}/install-dependency/", json={"package": package})
        return response.json()

    def uninstall_dependency(self, package):
        response = requests.post(f"{self.base_url}/uninstall-dependency/", json={"package": package})
        return response.json()
