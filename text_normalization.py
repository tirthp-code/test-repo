"""Small helpers for cleaning text before display."""

import re


def normalize_whitespace(text: str) -> str:
    """Trim text and replace whitespace runs with a single space.

    Handles Unicode whitespace, including tabs and line breaks. Empty or
    whitespace-only input returns an empty string.
    """
    return re.sub(r"\s+", " ", text).strip()
