"""Integer utility for functional test scenarios."""


def is_multiple_of_three(number: int) -> bool:
    """Detect integer multiples of three."""
    return number % 3 == 0
