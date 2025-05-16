def validate_positive_float(value: str) -> float:
    """Validates that the input string is a positive float."""
    try:
        val = float(value)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        raise ValueError(f"Invalid positive float: {value}")

def validate_positive_int(value: str) -> int:
    """Validates that the input string is a positive integer."""
    try:
        val = int(value)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        raise ValueError(f"Invalid positive integer: {value}")