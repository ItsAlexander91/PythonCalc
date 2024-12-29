def convert_units(value, choice):
    if choice == '1':
        return value / 1000  # Meters to Kilometers
    elif choice == '2':
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif choice == '3':
        return value / 1000  # Grams to Kilograms
    else:
        return "Invalid conversion choice."
