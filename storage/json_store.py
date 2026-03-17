import json
from datetime import datetime

FILE = "data.json"


def load() -> dict:
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"sets": {}, "history": []}


def save(data: dict) -> None:
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_entry(data: dict, operation: str, A: set, B: set | None, result) -> None:
    """Build a history entry and append it to data['history']."""

    # Serialize result
    if isinstance(result, set):
        # Could be a set of ints OR a set of tuples (cartesian product)
        sample = next(iter(result), None)
        if isinstance(sample, tuple):
            serialized_result = [list(pair) for pair in sorted(result)]
        else:
            serialized_result = sorted(result)
    else:
        serialized_result = result  # int for cardinality

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "operands": {
            "A": sorted(A),
            "B": sorted(B) if B is not None else None,
        },
        "result": serialized_result,
    }
    data["history"].append(entry)


def get_history(data: dict) -> list:
    return data.get("history", [])


def clear_history(data: dict) -> None:
    data["history"] = []
