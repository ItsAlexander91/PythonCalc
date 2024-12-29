# gui/app.py
import tkinter as tk
from operations.basic import add, subtract, multiply, divide

def start_gui():
    """Starts the calculator GUI."""
    def calculate():
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    # Create the main window
    root = tk.Tk()
    root.title("Ultimate Python Calculator")

    # Input fields
    tk.Label(root, text="Number 1:").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    tk.Label(root, text="Number 2:").grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    # Operation selection
    tk.Label(root, text="Operation:").grid(row=2, column=0)
    operation_var = tk.StringVar(value="+")
    tk.OptionMenu(root, operation_var, "+", "-", "*", "/").grid(row=2, column=1)

    # Calculate button
    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

    # Result display
    result_label = tk.Label(root, text="Result:")
    result_label.grid(row=4, column=0, columnspan=2)

    # Run the GUI loop
    root.mainloop()
