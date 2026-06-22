import subprocess
import sys
import time

def __init__(self, executable_path):
    self.executable_path = executable_path
    self.process = None

def start(self, arguments):
    print(f"[*] DPI Bypass tool is starting: {self.executable_path}")

    try:
        command = [self.executable_path] + arguments
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("[+] Service has been started successfully. Traffic is now hidden.")

    except FileNotFoundError:
        print("[-] Error: No  file found to execute. Check the path.")
        sys.exit(1)
    
    except Exception as e:
        print(f"[-] Error has been occured:{e}")
    
def stop(self):
    if self.process and self.process.poll() is None:
        print("\n [*] Stopping Service...")
        self.process.terminate()
        self.process.wait()
        print("[+] Service has been shut.")

if __name__ == "__main__":
    TOOL_PATH = "./goodbyedpi.exe"

    PARAMS = ["-5"]

    manager = TOOL_PATH

    try:
        manager.start(PARAMS)
        print("[*] To terminate use Ctrl+C.")
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        manager.stop()