import os
import webbrowser

def open_chrome():
    """Opens Google Chrome by navigating to Google."""
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens the Calculator application (Windows example)."""
    try:
        os.system("calc")
    except Exception as e:
        print("Error opening calculator:", e)

def open_notepad():
    """Opens Notepad (Windows example)."""
    try:
        os.system("notepad")
    except Exception as e:
        print("Error opening notepad:", e)

def cpu_usage():
    """Returns the current CPU usage percentage."""
    try:
        import psutil
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        print("Error retrieving CPU usage:", e)
        return None

def ram_usage():
    """Returns the current RAM usage percentage."""
    try:
        import psutil
        return psutil.virtual_memory().percent
    except Exception as e:
        print("Error retrieving RAM usage:", e)
        return None

def run_shell_command(cmd="echo Hello, world!"):
    """Executes a shell command and returns its output."""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print("Error running shell command:", e)
        return None
