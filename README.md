# DPI Evasion Service Manager

A small command-line helper I wrote for my own daily use on Windows. It starts and stops [GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI) from a simple menu and lets me switch between saved argument profiles. It's a personal project for basic use, so it may contain bugs.

<img width="457" height="262" alt="DPI Evasion Manager screenshot" src="https://github.com/user-attachments/assets/3ea4beb4-d5e8-4be6-952c-c5ebcacb20cb" />

## What it does

- Menu with four options: start, stop, change profile, exit
- Shows whether the service is running and which profile is active
- Prints GoodbyeDPI's output to the console from a background thread
- Profiles are stored in `config.json`; choosing a new profile saves it and, if GoodbyeDPI is running, restarts it with the new arguments
- Checks for administrator rights before starting, since GoodbyeDPI needs them

All the actual packet handling is done by GoodbyeDPI; this tool only manages it.

## Running it

Windows only. The tool is meant to be used through the prebuilt executable in the `dist` folder.

1. Download or clone the repository.
2. Copy `dist/DPI_Manager.exe` into the main project folder, so it sits next to `config.json`, `goodbyedpi.exe`, `WinDivert.dll` and `WinDivert64.sys`.
3. Right-click `DPI_Manager.exe` and choose **Run as administrator**.

The GoodbyeDPI files are included in the repository; you can also download them from the [official GoodbyeDPI releases](https://github.com/ValdikSS/GoodbyeDPI/releases).

## Profiles

Each profile in `config.json` is just the list of arguments passed to GoodbyeDPI:

```json
{
    "tool_path": "./goodbyedpi.exe",
    "active_profile": "default",
    "profiles": {
        "default": ["-5"],
        "aggresive": ["-9", "--dns-addr", "1.1.1.1", "--dns-port", "53"],
        "custom_speed": ["-e", "1", "-f", "1", "--reverse-frag"]
    }
}
```

You can add your own profiles; they show up in the menu automatically. See the GoodbyeDPI README for what each argument does.

## Limitations

- Windows only, tested only on my own machine.
- Made for simple personal use; error handling is basic.

Please make sure your use complies with the laws and network policies that apply to you. Suggestions and bug reports are welcome through Issues.

## License

MIT – see [LICENSE](LICENSE).
