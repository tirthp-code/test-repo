"""Small helpers for cleaning text before display."""

def normalize_whitespace(text: str) -> str:
    """Trim text and replace whitespace runs with a single space.

    Handles Unicode whitespace, including tabs and line breaks. Empty or
    whitespace-only input returns an empty string.
    """
    return " ".join(text.split())
