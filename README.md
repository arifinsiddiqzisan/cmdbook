# CmdBook

CmdBook is a terminal-based command manager that helps you organize, search, and execute your frequently used CLI commands through an interactive TUI (Text User Interface).

It is designed for developers and Linux users who frequently customize their workflow and want a reliable way to store and reuse commands.

---

## Features

* Interactive TUI with keyboard navigation
* Add, edit, and delete commands
* Run commands directly from the interface
* Persistent storage using JSON
* Lightweight and fast
* Clean and minimal interface

---

## Keybindings

| Key       | Action       |
| --------- | ------------ |
| Up / Down | Navigate     |
| Enter     | Select       |
| Ctrl + A  | Add command  |
| Ctrl + E  | Edit command |
| Ctrl + D  | Delete       |
| Ctrl + R  | Run command  |

---

## Use Cases

* Store frequently used Linux commands
* Manage development shortcuts
* Keep track of automation scripts
* Build a personal command knowledge base

---

## Installation

### Manual Installation

Clone the repository:

```bash
git clone https://github.com/arifinsiddiqzisan/cmdbook.git
cd cmdbook
```

Install dependencies:

```bash
pip install textual rich
```

Move the script to a system-wide location:

```bash
sudo mv cmdbook.py /usr/local/bin/cmdbook
```

Make it executable:

```bash
sudo chmod +x /usr/local/bin/cmdbook
```

Create the data directory:

```bash
mkdir -p ~/.cmdbook
```

Create the data file:

```bash
touch ~/.cmdbook/commands.json
echo "[]" > ~/.cmdbook/commands.json
```

Run the application:

```bash
cmdbook
```

---

### Alternative (User-only Installation)

If you prefer not to use `sudo`, install it locally:

```bash
mkdir -p ~/.local/bin
mv cmdbook.py ~/.local/bin/cmdbook
chmod +x ~/.local/bin/cmdbook
```

Ensure the path is available:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Then run:

```bash
cmdbook
```

---

## Requirements

* Python 3
* pip

Install pip if not available:

```bash
sudo apt install python3-pip
```

Install required Python packages:

```bash
pip install textual rich
```

---

## Data Storage

CmdBook stores all commands in:

```
~/.cmdbook/commands.json
```

This keeps your data separate from system files and avoids permission issues.

---

## Example Entry

```
Name: pyenv
Command: pyenv
Description: Manage Python virtual environments
```

---

## Tech Stack

* Python
* Textual
* Rich

---

## Philosophy

CmdBook is built with a simple idea:

Your terminal should remember what you forget.

Instead of searching for commands repeatedly, store them once and access them instantly.

---

## License

MIT License

---

## Contributing

Contributions are welcome. You can:

* Open issues
* Suggest features
* Submit pull requests

---

## Author

Arifin Siddiq Zisan
