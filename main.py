import subprocess
import sys
import time
import threading
import ctypes
import os

class DPIBypassManager:
    def __init__(self, executable_path):
        self.executable_path = executable_path
        self.process = None
        self.is_running = False

    def admin(self):
        try:
            if os.name == 'nt':
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
        
        except Exception:
            return False
    
    def read_logs(self):
        while self.is_running and self.process:
            line = self.process.stdout.readline()
            if line:
                    clean_line = line.strip()
                    print(f"[DPI-Engine] {clean_line}")

            if self.process.poll() is not None:
                break

    def start(self, arguments):
        if not self.is_admin():
            print("[-] Error: DPI must run as an administor.")
            sys.exit(1)
    
        print(f"[*] DPI Bypass tool is starting: {self.executable_path}")

        try:
            self.process = subprocess.Popen(
                [self.executable_path] + arguments,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            self.is_running=True

            log_thread = threading.Thread(target=self.read_logs, daemon=True)
            log_thread.start()

            print("[+] Service has been started successfully. Traffic is now hidden.")

        except FileNotFoundError:
            print("[-] Error: No  file found to execute. Check the path.")
            sys.exit(1)
    
    def stop(self):
        if self.process and self.process.poll() is None:
            print("\n [*] Stopping Service...")
            self.is_running = False
            self.process.terminate()
            self.process.wait()
            print("[+] Service has been shut.")

if __name__ == "__main__":
    TOOL_PATH = "./goodbyedpi.exe"
    PARAMS = ["-5"]

    manager = DPIBypassManager(TOOL_PATH)

    try:
        manager.start(PARAMS)
        print("[*] To terminate use Ctrl+C.")
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        manager.stop()
