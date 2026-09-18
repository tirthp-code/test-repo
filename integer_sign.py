"""Integer utility for functional test scenarios."""


def integer_sign(number: int) -> int:
    """Return the sign of an integer."""
    return (number > 0) - (number < 0)
