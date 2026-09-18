"""Read-only text inspection helpers."""

def count_blank_lines(text: str) -> int:
    """Count empty or whitespace-only lines using str.splitlines semantics."""
    return sum(not line or line.isspace() for line in text.splitlines())
