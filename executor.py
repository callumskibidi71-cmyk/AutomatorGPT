# executor.py
import subprocess
import platform

def run_command(command):
    try:
        # Detect OS (Windows vs Mac/Linux)
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)
