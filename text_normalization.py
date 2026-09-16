"""Small helpers for cleaning text before display."""


def normalize_whitespace(text: str) -> str:
    """Trim text and collapse consecutive whitespace to a single space.

    Spaces, tabs, line breaks, and other Unicode whitespace are normalized.
    Empty and whitespace-only strings produce an empty string.
    """
    return " ".join(text.split())
