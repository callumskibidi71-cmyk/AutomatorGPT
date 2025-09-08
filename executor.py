# executor.py
import subprocess
import platform

SAFE_COMMANDS = ["dir", "ls", "echo", "whoami", "date", "pwd"]  # Add more safe commands here

def is_safe_command(command):
    return any(command.strip().startswith(cmd) for cmd in SAFE_COMMANDS)

def run_command(command):
    if not is_safe_command(command):
        return "Command blocked: not considered safe."
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)
