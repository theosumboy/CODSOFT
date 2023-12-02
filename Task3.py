import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
        
        password = generate_password(length)
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
tk.Label(root, text="Password Length:").pack(pady=10)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack(pady=10)

# Button to generate and display password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=20)

# Label to display the generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12))
password_label.pack(pady=10)

# Run the main loop
root.mainloop()
