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

def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)

def main_menu():
    config = ConfigManager()
    tool_path = config.get_tool_path()

    if not tool_path:
        sys.exit(1)
    
    manager = DPIBypassManager(tool_path)

    while True:
        clear_screen()
        print("-----------------------------------")
        print("        DPI Evasion Manager        ")
        print("-----------------------------------")

        active_profile = config.config_data.get("active_profile", "Unknown")
        status = "🟢 ACTIVE (Running)" if manager.is_running else "🔴 PASSİVE (Stopped)"

        print(f"Status              : {status}")
        print(f"Active Profile      : {active_profile}")
        print("---------------------------------------")

        print("[1] Start Service")
        print("[2] Stop Service")
        print("[3] Change Profile")
        print("[4] Exit \n")

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            if not manager.is_running:
                params = config.get_activate_parameters()
                manager.start(params)
            else:
                print("\n[!] Service is already running!")
                time.sleep(2)
        
        elif choice == "2":
            if manager.is_running():
                manager.stop()
            else:
                print("[!] Service is already shut!")
                time.sleep(2)

        elif choice == "3":
            print("\n--- Avaliable Profiles ---")
            profiles = config.config_data.get("profiles",{})
            profile_names = list(profiles.keys())

            for index, profile_name in enumerate(profile_names,1):
                print(f"[{index}] {profile_name}")
            
            try:
                profile_choice = int(input("\n Enter the number of desired profile: "))
                if 1 <= profile_choice <= len(profile_names):
                    new_profile = profile_names[profile_choice-1]

                    config.config_data["activate_profile"] = new_profile

                    with open(config.config_file,"w",encoding="utf-8") as f:
                        json.dump(config.config_data,f,indent=4)

                    print(f"\n[+] The profile has been updated to ‘{new_profile}’!")

                    if manager.is_running:
                        print("[*] The service is restarting to apply the changes...")
                        manager.stop()
                        manager.start(config.get_activate_parameters())
                else:
                    print("\n Invalid Choice.")

            except ValueError:
                print("\n[-] Enter a valid number.")
            
            time.sleep(2)

        elif choice == "4":
            print("\n[*] Exiting...")
            if manager.is_running:
                manager.stop()
            sys.exit(0)

        else:
            print("\n[-] Invalid Choice, try again.")
            time.sleep(1)
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[*] Forced to stop. Cleaning...")
        sys.exit(0)
                
