# utils/validator.py

def validate_number(value):
    """Check if the input is a valid number."""
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid number! Please enter a numeric value.")

def validate_choice(choice, valid_choices):
    """Check if the choice is within the valid options."""
    if choice in valid_choices:
        return choice
    raise ValueError(f"Invalid choice! Valid options are: {', '.join(valid_choices)}")
