"""Read-only text inspection helpers."""

def count_whitespace(text: str) -> int:
    """Return the number of whitespace code points without rewriting text."""
    return sum(character.isspace() for character in text)
