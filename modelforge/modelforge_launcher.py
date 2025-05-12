
import subprocess

def launch_model(path, api_port=11434):
    return subprocess.Popen(["ollama", "run", path, "--port", str(api_port)])
