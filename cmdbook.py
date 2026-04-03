#!/usr/bin/env python3

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Static, Input, Button
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from rich.text import Text
import json, os, platform


# ------------------ PATH SETUP ------------------
if platform.system() == "Windows":
    BASE_DIR = os.path.join(os.environ["USERPROFILE"], "cmdbook")
else:
    BASE_DIR = os.path.join(os.path.expanduser("~"), ".cmdbook")

FILE = os.path.join(BASE_DIR, "commands.json")


# ------------------ DATA ------------------
def load():
    os.makedirs(BASE_DIR, exist_ok=True)

    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)

    with open(FILE) as f:
        return json.load(f)


def save(data):
    os.makedirs(BASE_DIR, exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


# ------------------ FORM SCREEN ------------------
class FormScreen(Screen):
    def __init__(self, mode="add", data=None):
        super().__init__()
        self.mode = mode
        self.data = data or {}

    def compose(self):
        yield Vertical(
            Static(f"{self.mode.upper()} COMMAND", classes="title"),
            Input(value=self.data.get("name", ""), placeholder="Name", id="name"),
            Input(value=self.data.get("command", ""), placeholder="Command", id="cmd"),
            Input(value=self.data.get("description", ""), placeholder="Description", id="desc"),
            Horizontal(
                Button("Save", id="save"),
                Button("Cancel", id="cancel"),
            ),
        )

    def on_button_pressed(self, event):
        if event.button.id == "cancel":
            self.app.pop_screen()
            return

        name = self.query_one("#name").value.strip()
        cmd = self.query_one("#cmd").value.strip()
        desc = self.query_one("#desc").value.strip()

        if not name or not cmd:
            return

        data = load()

        if self.mode == "add":
            data.append({"name": name, "command": cmd, "description": desc})

        elif self.mode == "edit":
            for item in data:
                if item["name"] == self.data["name"]:
                    item["name"] = name
                    item["command"] = cmd
                    item["description"] = desc

        save(data)
        self.app.pop_screen()
        self.app.refresh_list()


# ------------------ MAIN APP ------------------
class CmdBook(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    .title {
        text-align: center;
        padding: 1;
        background: #444;
        color: white;
    }

    ListView {
        border: solid #666;
        width: 40%;
    }

    #details {
        border: solid #666;
        padding: 1;
        width: 60%;
        height: 100%;
        overflow: auto;
    }
    """

    BINDINGS = [
        ("ctrl+a", "add", "Add"),
        ("ctrl+e", "edit", "Edit"),
        ("ctrl+d", "delete", "Delete"),
        ("ctrl+r", "run", "Run"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            ListView(id="list"),
            Static("Select a command...", id="details"),
        )
        yield Footer()

    def on_mount(self):
        self.refresh_list()

    # -------- Refresh List --------
    def refresh_list(self):
        self.data = load()
        self.selected = None

        list_view = self.query_one("#list", ListView)
        list_view.clear()

        for cmd in self.data:
            item = ListItem(Static(cmd["name"]))
            item.cmd_data = cmd
            list_view.append(item)

    # -------- Selection --------
    def on_list_view_selected(self, event):
        self.selected = event.item.cmd_data
        cmd = self.selected

        text = Text()
        text.append(f"Name: {cmd['name']}\n\n", style="bold")
        text.append("Command:\n", style="cyan bold")
        text.append(f"{cmd['command']}\n\n", style="cyan")
        text.append("Description:\n", style="yellow bold")
        text.append(cmd["description"])

        self.query_one("#details").update(text)

    # -------- Actions --------
    def action_add(self):
        self.push_screen(FormScreen("add"))

    def action_edit(self):
        if self.selected:
            self.push_screen(FormScreen("edit", self.selected))

    def action_delete(self):
        if not self.selected:
            return

        data = load()
        data = [c for c in data if c["name"] != self.selected["name"]]
        save(data)

        self.refresh_list()

    def action_run(self):
        if self.selected:
            os.system(self.selected["command"])


# ------------------ RUN ------------------
def main():
    CmdBook().run()


if __name__ == "__main__":
    main()