"""Read-only text inspection helpers."""

def has_whitespace(text: str) -> bool:
    """Return whether any code point is Unicode whitespace."""
    return any(character.isspace() for character in text)
