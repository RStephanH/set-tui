from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Static, DataTable, Footer
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from core.operations import union, intersection, cardinality, cartesian_product
from storage.json_store import load, save, add_entry, get_history, clear_history


# ─────────────────────────────────────────────
#  History Screen
# ─────────────────────────────────────────────
class HistoryScreen(Screen):
    CSS = """
    HistoryScreen {
        align: center middle;
    }
    #history-container {
        width: 90%;
        height: 80%;
        border: round cyan;
        padding: 2;
    }
    #history-title {
        text-align: center;
        color: cyan;
        text-style: bold;
        margin-bottom: 1;
    }
    DataTable {
        height: 1fr;
    }
    #history-buttons {
        align: center middle;
        margin-top: 1;
    }
    #close-history {
        margin: 1;
        width: 20;
    }
    #clear-history {
        margin: 1;
        width: 20;
        background: red;
        color: white;
    }
    """

    def __init__(self, data: dict):
        super().__init__()
        self.data = data

    def compose(self) -> ComposeResult:
        with Vertical(id="history-container"):
            yield Static("📜 Operation History", id="history-title")
            yield DataTable(id="history-table")
            with Horizontal(id="history-buttons"):
                yield Button("← Back", id="close-history")
                yield Button("🗑 Clear History", id="clear-history")

    def on_mount(self) -> None:
        table = self.query_one("#history-table", DataTable)
        table.add_columns("Time", "Operation", "Set A", "Set B", "Result")
        self._populate(table)

    def _populate(self, table: DataTable) -> None:
        table.clear()
        history = get_history(self.data)
        if not history:
            table.add_row("—", "No history yet", "—", "—", "—")
            return
        for entry in reversed(history):  # newest first
            table.add_row(
                entry.get("timestamp", "—"),
                entry.get("operation", "—"),
                str(entry["operands"].get("A", "—")),
                str(entry["operands"].get("B"))
                if entry["operands"].get("B") is not None
                else "—",
                str(entry.get("result", "—")),
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "close-history":
            self.app.pop_screen()
        elif event.button.id == "clear-history":
            clear_history(self.data)
            save(self.data)
            table = self.query_one("#history-table", DataTable)
            self._populate(table)
            self.app.notify("History cleared 🗑")


# ─────────────────────────────────────────────
#  Main App
# ─────────────────────────────────────────────
class SetApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #main {
        width: 60%;
        border: round cyan;
        padding: 2;
    }
    #title {
        text-align: center;
        color: cyan;
        text-style: bold;
        margin-bottom: 1;
    }
    Input {
        margin: 1;
        border: solid green;
    }
    Button {
        margin: 1;
        width: 20;
    }
    .button-row {
        align: center middle;
    }
    #result {
        margin-top: 2;
        border: heavy yellow;
        padding: 1;
        color: yellow;
        text-align: center;
    }
    #quit {
        background: red;
        color: white;
    }
    #save {
        background: green;
        color: black;
    }
    #history-btn {
        background: dodgerblue;
        color: white;
    }
    """
    BINDINGS = [("q", "quit", "Quit"), ("h", "show_history", "History")]

    # ── Lifecycle ──────────────────────────────
    def on_mount(self) -> None:
        self.data = load()
        if "history" not in self.data:
            self.data["history"] = []
        if "sets" not in self.data:
            self.data["sets"] = {}

    # ── Layout ─────────────────────────────────
    def compose(self) -> ComposeResult:
        with Vertical(id="main"):
            yield Static("📊 Set Operations App", id="title")
            yield Input(placeholder="Set A:  1 2 3", id="A")
            yield Input(placeholder="Set B:  3 4 5", id="B")

            with Horizontal(id="buttons-row1", classes="button-row"):
                yield Button("Union", id="union")
                yield Button("Intersection", id="inter")
                yield Button("Cardinality", id="card")

            with Horizontal(id="buttons-row2", classes="button-row"):
                yield Button("Cartesian Product", id="prod")

            yield Static("Result will appear here", id="result")

            with Horizontal(id="buttons-actions", classes="button-row"):
                yield Button("💾 Save", id="save")
                yield Button("📜 History", id="history-btn")
                yield Button("🚪 Quit", id="quit")
        yield Footer()

    # ── Button handler ─────────────────────────
    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = event.button.id

        if btn == "quit":
            save(self.data)
            self.notify("Saved & exiting... 💾")
            self.exit()
            return

        if btn == "save":
            save(self.data)
            self.notify("Data saved 💾")
            return

        if btn == "history-btn":
            self.action_show_history()
            return

        # ── Operation buttons ──
        try:
            raw_a = self.query_one("#A", Input).value.strip()
            raw_b = self.query_one("#B", Input).value.strip()

            if not raw_a:
                raise ValueError("Set A is empty")

            A = set(map(int, raw_a.split()))
            B = set(map(int, raw_b.split())) if raw_b else set()

            res = None
            b_used = None  # track whether B was actually needed

            if btn == "union":
                res = union(A, B)
                b_used = B
            elif btn == "inter":
                res = intersection(A, B)
                b_used = B
            elif btn == "card":
                res = cardinality(A)
                b_used = None  # cardinality only uses A
            elif btn == "prod":
                res = cartesian_product(A, B)
                b_used = B

            if res is None:
                return

            self.query_one("#result", Static).update(f"✅ Result: {res}")

            # Persist the full entry
            add_entry(self.data, btn, A, b_used, res)
            self.notify("Operation success ✅")

        except ValueError as e:
            self.query_one("#result", Static).update(f"⚠️ Input Error: {e}")
            self.notify("Invalid input ❌")
        except Exception as e:
            self.query_one("#result", Static).update(f"⚠️ Error: {e}")
            self.notify("Operation failed ❌")

    # ── Actions ────────────────────────────────
    def action_show_history(self) -> None:
        self.push_screen(HistoryScreen(self.data))

    def action_quit(self) -> None:
        save(self.data)
        self.exit()
