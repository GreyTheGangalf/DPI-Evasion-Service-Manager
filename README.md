# DPI Evasion Service Manager 🛡️

A robust, object-oriented Python wrapper designed to manage Deep Packet Inspection (DPI) evasion tools (such as GoodbyeDPI). It features dynamic configuration, real-time log monitoring, and an interactive CLI, packaged as a standalone executable.

## 🚀 Overview
Internet Service Providers (ISPs) often use DPI to block access to specific websites or services (like Discord) by inspecting the Server Name Indication (SNI) in data packets. 

While core tools like GoodbyeDPI can bypass these restrictions via packet fragmentation and TCP header manipulation, they operate purely via complex command-line arguments. **DPI Evasion Service Manager** acts as an intelligent layer over these core tools. It provides a state-managed CLI interface, dynamic JSON-based configuration, and automated OS-level privilege checks, making DPI evasion accessible, configurable, and crash-resistant.

## ✨ Key Features
* **State Management & Interactive CLI:** A clean command-line interface to start, stop, and monitor the evasion engine without restarting the application.
* **Dynamic Profiling (JSON):** Easily switch between different evasion strategies (e.g., default, aggressive) on the fly via a `config.json` file.
* **Asynchronous Log Handling:** Utilizes Python's `threading` module to read the underlying engine's output in real-time without blocking the main application loop.
* **Automated Privilege Escalation:** Checks for Windows Administrator rights natively via `ctypes` and enforces them to ensure `WinDivert` network drivers function correctly.
* **Standalone Executable:** Compiled using PyInstaller for a seamless plug-and-play experience without requiring a local Python environment.

## 🛠️ Architecture & Under the Hood
This project applies the **Wrapper Pattern**. It uses Python's `subprocess` module to spawn and control low-level C/C++ network executables. 
* The `DPIBypassManager` class acts as the core engine, handling process lifecycle (`Popen`, `terminate`, `wait`) and pipe redirection.
* The `ConfigManager` isolates file I/O operations, ensuring that the application logic remains decoupled from data storage.

## 📦 Installation & Usage

### Option 1: Pre-compiled Release (Recommended)
1. Go to the **[Releases](../../releases)** tab on this repository.
2. Download the latest `DPI_Manager_V1.zip` file.
3. Extract the folder to your desktop. Ensure `DPI_Manager.exe`, `goodbyedpi.exe`, `WinDivert.dll`, and `WinDivert64.sys` are in the same directory.
4. Double click `DPI_Manager.exe`. (It will automatically prompt for UAC Admin privileges).

### Option 2: Running from Source
If you want to run or build the project from the source code:
```bash
# Clone the repository
git clone [https://github.com/GreyThegANGALF/dpi-evasion-manager.git](https://github.com/GreyTheGangalf/dpi-evasion-manager.git)
cd dpi-evasion-manager

# Ensure you place the required GoodbyeDPI binaries in the root folder:
# - goodbyedpi.exe
# - WinDivert.dll
# - WinDivert64.sys

# Run with administrative privileges
python main.py
⚙️ Configuration (config.json)
The tool behavior is controlled by the configuration file. You can add as many custom profiles as you want.

JSON
{
    "tool_path": "./goodbyedpi.exe",
    "active_profile": "default",
    "profiles": {
        "default": ["-5"],
        "aggressive": ["-9", "--dns-addr", "1.1.1.1", "--dns-port", "53"],
        "custom_fast": ["-e", "1", "-f", "1", "--reverse-frag"]
    }
}
Tip: If you are experiencing ERR_CONNECTION_TIMED_OUT, try switching to the aggressive profile and ensure Secure DNS (DoH) is enabled in your browser.

🗺️ Roadmap
V1: CLI Interface, JSON Config, Subprocess Wrapper (Current)

V2: Migration to a modern graphical user interface (GUI) utilizing Next.js, Tailwind CSS, and Tauri for a seamless desktop experience.

⚠️ Disclaimer
This project is developed strictly for educational purposes and to demonstrate systems programming, process management, and network protocol concepts. The developer assumes no liability for the misuse of this software. Please respect the terms of service of your network provider.

This project is a Python wrapper. The core DPI evasion functionality is powered by GoodbyeDPI and packet diversion is handled by WinDivert. All credits for the underlying binaries go to their respective original authors.

This is NOT a VPN

Please note that **DPI Evasion Manager** is designed solely to bypass Deep Packet Inspection (DPI) systems used by Internet Service Providers. It works by manipulating packet fragmentation and SNI headers at the local level.

* **No IP Masking:** This tool does **not** change, hide, or mask your real IP address.
* **No Traffic Encryption:** Unlike a traditional VPN, it does **not** encrypt your overall network traffic.
* **No Privacy/Anonymity Guarantee:** It does not provide secure browsing, anonymity, or protection against third-party tracking, malicious actors, or network monitoring.

Use this tool responsibly and understand that your destination traffic is still fundamentally visible to the network nodes you pass through. If you require absolute privacy, data encryption, and anonymity, please use a trusted and secure VPN service.
