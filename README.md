<div align="center">

# Smart File Organizer

**Automatically organize your Windows Desktop files by file type.**

<!-- Customize these badges to match your project -->
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Status](https://img.shields.io/badge/Project-First%20Release-orange?style=for-the-badge)

<!-- Add a screenshot after capturing one -->
<!-- ![Smart File Organizer screenshot](assets/screenshot.png) -->

</div>

---

## Overview

**Smart File Organizer** is a Python script that monitors the Windows Desktop and moves supported files into folders based on their extensions. It also writes activity messages to a log file and can play a sound after moving a file.

> **Important:** This script moves files out of the Desktop. Test it with unimportant sample files before using it with real files.

## Features

- Monitors the Desktop periodically.
- Sorts supported files into category folders.
- Creates category folders when they do not exist.
- Records activity in `organizer_log.txt`.
- Plays a Windows beep after a successful move.
- Can be configured to start when you sign in to Windows.

## File categories

These categories are currently configured in the script:

| File types | Destination folder |
|---|---|
| `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp` | `imgas` |
| `.txt`, `.pdf`, `.docx`, `.doc`, `.pptx`, `.xlsx` | `Noat` |
| `.zip`, `.rar`, `.7z`, `.tar` | `Archives` |
| `.mp4`, `.mp3`, `.mkv`, `.avi`, `.wav` | `Media` |

The folder names match the current code. You can rename them in the `categories` dictionary in `tst.py`.

## Requirements

- Windows
- Python 3
- No third-party Python packages are required by the current script.

The script uses `winsound`, which is available on Windows.

## Run the script

1. Download or clone this repository.
2. Open Command Prompt in the folder containing `tst.py`.
3. Run:

```bash
python tst.py
```

The program keeps running and checks the Desktop every two seconds. To stop it, press `Ctrl + C` in the terminal.

## Start automatically on Windows sign-in

You can use the Windows Startup folder:

1. Press `Win + R`.
2. Enter `shell:startup`.
3. Create a `.bat` file in that folder, for example `start_organizer.bat`.
4. Put the following in the file, replacing the example path with the real path to `tst.py`:

```bat
@echo off
python "C:\Path\To\tst.py"
```

This starts the script when you sign in to Windows, provided the `python` command is available. The terminal window may remain open while the script runs.

## Log file

The script writes its log to:

```text
Desktop/organizer_log.txt
```

The log includes timestamps and messages about program startup, moved files, and stopping the program.

## Current limitations

- Only the extensions listed in the script are organized.
- The script monitors the Desktop only.
- Files are moved, not copied.
- If a destination already contains a file with the same name, the current code does not explicitly handle that name conflict. Test carefully before relying on it.
- The current script uses fixed folder names and does not have a graphical interface yet.

## Roadmap

- [ ] Add safer handling for duplicate filenames.
- [ ] Add a preview or confirmation mode before moving files.
- [ ] Improve folder names and make categories configurable.
- [ ] Add a graphical user interface.
- [ ] Package the script as a Windows `.exe`.

## Project structure

```text
SmartFileOrganizer/
├── tst.py
├── README.md
└── organizer_log.txt  # created on the Desktop when the script runs
```

## Contributing

Suggestions and bug reports are welcome. If you want to contribute, open an issue describing the change or improvement.

## License

No license has been selected for this project yet. Add a license before allowing others to reuse, modify, or distribute the code.

---

<div align="center">

Made with Python on Windows.

</div>
