# DPI Evasion Service Manager 🛡️

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux-lightgrey?style=flat-square)
![Stars](https://img.shields.io/github/stars/GreyTheGangalf/DPI-Evasion-Service-Manager?style=flat-square)

> **Production-Grade Network Packet Manipulation System Manager** — Research-focused tool for analyzing network packet filtering mechanisms with sophisticated state management and dynamic configuration switching.

<img width="457" height="262" alt="Ekran görüntüsü 2026-08-27 140449" src="https://github.com/user-attachments/assets/3ea4beb4-d5e8-4be6-952c-c5ebcacb20cb" />

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. It is designed to help network engineers and security researchers understand packet manipulation techniques and network filtering mechanisms. Users are responsible for complying with applicable laws and regulations in their jurisdiction. Unauthorized access to computer networks is illegal.

---

## 🎯 What This Project Does

DPI Evasion Service Manager is a **production-grade Python wrapper** that manages network packet manipulation research systems with:

- **Dynamic configuration switching** without process restart
- **State management system** for handling multiple profiles
- **Real-time log monitoring** with asynchronous threading
- **Secure privilege escalation** with automated checks
- **Compiled executable deployment** for end-user distribution

---

## ✨ Key Features

### 1️⃣ Interactive CLI System
- **Real-time monitoring** of network packet operations
- **Dynamic profile switching** — Change evasion strategies without restarting
- **Live log streaming** using Python threading and async operations
- **User-friendly menus** for configuration management

### 2️⃣ Advanced State Management
```python
# State Handling Example
{
  "profiles": {
    "aggressive": {
      "packet_size": 1280,
      "timeout": 5000,
      "retry_count": 3
    },
    "conservative": {
      "packet_size": 512,
      "timeout": 10000,
      "retry_count": 5
    }
  },
  "active_profile": "conservative"
}
```

### 3️⃣ Secure .exe Compilation
- **PyInstaller integration** for standalone executable generation
- **Administrative privilege checks** using ctypes
- **Zero external dependencies** for end-users (batteries included)
- **Portable distribution** without requiring Python installation

### 4️⃣ Asynchronous Log Monitoring
- **Threading-based real-time output** streaming
- **Event-driven system** for graceful shutdown
- **Circular buffer logging** to prevent memory overflow
- **Color-coded console output** for better readability

### 5️⃣ Research-Focused Architecture
- **Modular design** for easy extension and customization
- **GoodbyeDPI integration** for packet manipulation research
- **Clean separation** between logic and UI layers
- **Extensive error handling** for network resilience

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────┐
│           User Input (CLI Menu)                │
└────────────────┬─────────────────────────────┘
                 │
                 ▼
     ┌──────────────────────────┐
     │  State Management Layer  │
     │  (JSON Configuration)    │
     └────────────┬─────────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
        ▼                    ▼
   ┌─────────────┐    ┌─────────────┐
   │   Profile   │    │  Subprocess │
   │  Selection  │    │  Management │
   │             │    │ (GoodbyeDPI)│
   └─────────────┘    └─────────────┘
        │                    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │  Threading Events    │
        │  Log Streaming       │
        │  Real-time Monitoring│
        └──────────────────────┘
```

---

## 🔧 Technical Deep Dive

### State Management System

DPI uses JSON-based configuration profiles that can be switched dynamically:

```python
# Load configuration
config = load_config("profiles.json")

# Switch active profile
set_active_profile("aggressive")

# Monitor in real-time
monitor_logs()
```

### Subprocess Orchestration

Leverages Python's subprocess module to:
- Launch GoodbyeDPI with specific parameters
- Capture stdout/stderr in real-time
- Handle process signals gracefully
- Clean up resources on exit

### Privilege Escalation Handling

Uses ctypes to check and manage Windows administrative privileges:

```python
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False
```

### Threading-Based Log Streaming

Implements thread-safe event flags for cancellation:

```python
import threading

stop_event = threading.Event()

def read_logs():
    while not stop_event.is_set():
        # Read and display logs
        pass
```

---

## 📦 Installation

### Prerequisites
- **Python 3.8+** (for running from source)
- **Windows 7+** (for .exe version)
- **Administrative privileges** (for packet manipulation operations)

### Option 1: Executable (Recommended)

1. Download the latest `.exe` from [Releases](https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager/releases)
2. Run with administrative privileges
3. No Python installation required

```bash
# Right-click → Run as administrator
DPI-Service-Manager.exe
```

### Option 2: Run from Source

```bash
# 1. Clone repository
git clone https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager.git
cd DPI-Evasion-Service-Manager

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run with admin privileges
python main.py
```

### Option 3: Build Your Own Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --collect-all GoodbyeDPI main.py

# Output: dist/DPI-Service-Manager.exe
```

---

## 🚀 Usage Guide

### Basic Operation

1. **Launch Application**
   ```bash
   python main.py
   # OR run .exe with administrator privileges
   ```

2. **Select Profile**
   ```
   ┌─ DPI Service Manager ─┐
   │ 1. Aggressive Mode     │
   │ 2. Conservative Mode   │
   │ 3. Custom Profile      │
   │ 4. View Logs          │
   │ 5. Exit               │
   └───────────────────────┘
   ```

3. **Monitor in Real-Time**
   - Watch live packet manipulation logs
   - Switch profiles without restart
   - Check status and error conditions

4. **Graceful Shutdown**
   - Press Ctrl+C to stop cleanly
   - All threads terminated safely
   - Resources properly cleaned up

### Configuration File (profiles.json)

```json
{
  "profiles": {
    "aggressive": {
      "packet_size": 1280,
      "timeout": 5000,
      "http_mode": true,
      "description": "Maximum evasion - higher resource usage"
    },
    "conservative": {
      "packet_size": 512,
      "timeout": 10000,
      "http_mode": false,
      "description": "Stable operation - lower resource usage"
    },
    "custom": {
      "packet_size": 768,
      "timeout": 7500,
      "http_mode": true,
      "description": "User-defined profile"
    }
  },
  "active_profile": "conservative",
  "log_retention": 1000
}
```

---

## 💻 Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.8+ |
| **Subprocess Management** | Python subprocess module |
| **Concurrency** | Python threading |
| **Configuration** | JSON |
| **Privilege Handling** | ctypes (Windows) |
| **Core Research Tool** | GoodbyeDPI |
| **Packaging** | PyInstaller |

---

## 📊 Performance Characteristics

| Metric | Value | Notes |
|--------|-------|-------|
| **Memory Usage** | 15-30 MB | Depends on profile |
| **CPU Usage** | 5-15% | Dynamic packet processing |
| **Startup Time** | <2 seconds | Quick profile switching |
| **Log Buffer Size** | ~1000 entries | Circular buffer |
| **Supported Platforms** | Windows 7+ | Linux support planned |

---

## 🔬 Research Use Cases

### Network Engineering
- Study packet filtering mechanisms
- Analyze DPI system behavior
- Test network resilience

### Security Research
- Understand evasion techniques
- Document mitigation strategies
- Academic network research

### Educational Purposes
- Learn subprocess management in Python
- Understand threading and synchronization
- Study privilege escalation patterns

---

## 🤝 Contributing

Want to improve DPI Service Manager? We welcome contributions!

### Ways to Contribute

1. **Report Bugs** → Create an [Issue](https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager/issues)
2. **Submit Code** → Create a [Pull Request](https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager/pulls)
3. **Improve Docs** → Help with documentation

### Development Setup

```bash
# Fork & clone
git clone https://github.com/YOUR_USERNAME/DPI-Evasion-Service-Manager.git
cd DPI-Evasion-Service-Manager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Create feature branch
git checkout -b feature/your-feature

# Make changes, test, commit
pytest
black .
flake8 .

# Push and create Pull Request
git push origin feature/your-feature
```

---

## 📈 Roadmap

- [x] v1.0 — Core service manager with GoodbyeDPI wrapper
- [x] v1.1 — Dynamic profile switching without restart
- [x] v1.2 — Real-time log monitoring with threading
- [ ] **v1.3 — Coming Soon**
  - [ ] Multi-profile batch operations
  - [ ] Detailed statistics dashboard
  - [ ] Configuration backup/restore
  - [ ] Performance metrics tracking
- [ ] **v2.0 — Future**
  - [ ] Linux support
  - [ ] Web dashboard interface
  - [ ] API for programmatic control
  - [ ] Advanced filtering options

---

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Lint code
flake8 src/

# Format code
black src/
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

By using this software, you agree to comply with all applicable laws and regulations in your jurisdiction.

---

## 🙏 Acknowledgments

- **GoodbyeDPI** — Packet manipulation research tool
- **Python Community** — For threading, subprocess, and ctypes modules
- **Research Community** — For guidance on network engineering best practices

---

## ⚖️ Legal Notice

This software is provided for **educational and research purposes only**. Users are solely responsible for ensuring their use complies with:
- Local and international laws
- Network policies and terms of service
- Institutional guidelines (if applicable)

Unauthorized access to computer networks is illegal. Use responsibly.

---

## 📞 Get in Touch

- **GitHub Issues** → [Report bugs](https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager/issues)
- **Discussions** → [Chat & ideas](https://github.com/GreyTheGangalf/DPI-Evasion-Service-Manager/discussions)

- **LinkedIn** → [Erkin Arıkan](https://www.linkedin.com/in/erkin-arikan)

---

## ⭐ Show Your Support

If this project helped your research or learning, consider giving it a ⭐ on GitHub!

```
🌟 Star Count: Support us!
📥 Repository: Research & Education
👥 Contributors: Welcome!
```

---

**Made with ❤️ by [GreyTheGangalf](https://github.com/GreyTheGangalf)**

*For research and educational purposes. Use responsibly and legally.*
