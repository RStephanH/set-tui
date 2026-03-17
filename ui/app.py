from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Static
from textual.containers import Vertical, Horizontal
from core.operations import *
from storage.json_store import load, save


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
    }
    #quit {
        background: red;
        color: white;
    }
    #save {
        background: green;
        color: black;
    }
    """
    BINDINGS = [("q", "quit", "Quitter")]

    def on_mount(self):
        self.data = load()
        # Guard: ensure 'historique' key always exists
        if "historique" not in self.data:
            self.data["historique"] = []

    def compose(self) -> ComposeResult:
        with Vertical(id="main"):
            yield Static("📊 Set Operations App", id="title")

            # Inputs
            yield Input(placeholder="A: 1 2 3", id="A")
            yield Input(placeholder="B: 3 4 5", id="B")

            # Buttons row 1 — unique id "buttons-row1"
            with Horizontal(id="buttons-row1", classes="button-row"):
                yield Button("Union", id="union")
                yield Button("Intersection", id="inter")
                yield Button("Cardinality", id="card")

            # Buttons row 2 — unique id "buttons-row2"
            with Horizontal(id="buttons-row2", classes="button-row"):
                yield Button("Cartesian Product", id="prod")

            # Result display
            yield Static("Result here", id="result")

            # Action buttons — unique id "buttons-actions"
            with Horizontal(id="buttons-actions", classes="button-row"):
                yield Button("Save", id="save")
                yield Button("Quit", id="quit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            save(self.data)
            self.notify("Saving before exit... 💾")
            self.exit()
            return

        if event.button.id == "save":
            save(self.data)
            self.notify("Data saved 💾")
            return

        try:
            A = set(map(int, self.query_one("#A", Input).value.split()))
            B = set(map(int, self.query_one("#B", Input).value.split()))

            res = None
            if event.button.id == "union":
                res = union(A, B)
            elif event.button.id == "inter":
                res = intersection(A, B)
            elif event.button.id == "card":
                res = cardinality(A)
            elif event.button.id == "prod":
                res = cartesian_product(A, B)

            if res is None:
                return

            self.query_one("#result", Static).update(f"Result: {res}")

            # Serialize result safely for JSON storage
            if isinstance(res, set):
                serializable = sorted(list(res))
            elif isinstance(res, (set, frozenset)):
                # Cartesian product: set of tuples
                serializable = [list(pair) for pair in res]
            else:
                serializable = res

            self.data["History"].append(
                {
                    "operation": event.button.id,
                    "result": serializable,
                }
            )
            self.notify("Operation success ✅")

        except ValueError:
            self.query_one("#result", Static).update(
                "Input Error ⚠️ — enter integers only"
            )
            self.notify("Operation failed ❌")
        except Exception as e:
            self.query_one("#result", Static).update(f"Error ⚠️: {e}")
            self.notify("Operation failed ❌")

    def action_quit(self) -> None:
        save(self.data)
        self.exit()
