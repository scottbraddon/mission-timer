import tkinter as tk
from tkinter import ttk, messagebox

def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        product = a * b
        result_var.set(f"Result: {product}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Set up the main window
root = tk.Tk()
root.title("Multiplier")

# Input fields
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0)

ttk.Label(frame, text="First number:").grid(row=0, column=0, sticky="e")
entry1 = ttk.Entry(frame, width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Second number:").grid(row=1, column=0, sticky="e")
entry2 = ttk.Entry(frame, width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Multiply button
multiply_btn = ttk.Button(frame, text="Multiply", command=multiply)
multiply_btn.grid(row=2, column=0, columnspan=2, pady=(10,0))

# Result display
result_var = tk.StringVar(value="Result: ")
result_label = ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=2, pady=(10,0))

# Run the app
root.mainloop()
