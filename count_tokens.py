"""Read-only text inspection helpers."""

def count_tokens(text: str) -> int:
    """Return the number of whitespace-delimited tokens without rewriting text."""
    return len(text.split())
