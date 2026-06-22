import subprocess
import sys
import time
import threading
import ctypes
import os
import json

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

class ConfigManager:
    def __init__(self,config_file="config.json"):
        self.config_file =config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            print(f"[-] Error: {self.config_file} can't found!")
            return None
        
        try:
            with open(self.config_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("[-] Error: JSON file format is invalid.")
            return None
    
    def get_tool_path(self):
        return self.config_data.get("tool_path","./goodbyeapi.exe") if self.config_data else None
    
    def get_activate_parameters(self):
        if not self.config_data:
            return []
        activate_profile = self.config_data.get("activate_profile")
        profiles = self.config_data.get("profiles",{})

        if activate_profile in profiles:
            print(f"[+] '{activate_profile}' profile has been loaded.")
            return profiles [activate_profile]
        else:
            print(f"[-] Error: '{activate_profile}' can't found. Default parammeters will be used.")
            return [-5]