import tkinter as tk

root = tk.Tk()
root.title("Scale Example")
root.geometry("300x200")

# Function to display the current value of the scale
def show_value(val):
    value_label.config(text=f"Value: {val}")

# Create a Scale widget
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=show_value)
scale.pack(pady=20)

# Label to show the current value
value_label = tk.Label(root, text="Value: 0")
value_label.pack()

root.mainloop()
