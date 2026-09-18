"""Read-only text inspection helpers."""

def count_content(text: str) -> int:
    """Return the number of non-whitespace code points in the original text."""
    return sum(not character.isspace() for character in text)
