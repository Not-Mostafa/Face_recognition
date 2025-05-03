import tkinter as tk
from tkinter import ttk

def on_sign_in():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Attempting sign in with Username: {username}, Password: {password}")

# Create main window
root = tk.Tk()
root.title("Attendance Taker")
root.geometry("400x300")

# Title
title_label = ttk.Label(root, text="Attendance Taker", font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

# Separator
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=20, pady=5)

# Sign in frame
sign_in_frame = ttk.LabelFrame(root, text="Sign in", padding=(20, 10))
sign_in_frame.pack(padx=20, pady=10, fill='both', expand=True)

# Instruction label
instruction_label = ttk.Label(sign_in_frame, text="Enter your email and password")
instruction_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Username label and entry
username_label = ttk.Label(sign_in_frame, text="Username:")
username_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
username_entry = ttk.Entry(sign_in_frame)
username_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
username_entry.insert(0, "o")  # Pre-fill with "o" as in your image

# Password label and entry
password_label = ttk.Label(sign_in_frame, text="Password:")
password_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
password_entry = ttk.Entry(sign_in_frame, show="*")
password_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5)

# Sign in button
sign_in_button = ttk.Button(sign_in_frame, text="Sign in", command=on_sign_in)
sign_in_button.grid(row=3, column=0, columnspan=2, pady=10)

# Configure grid weights
sign_in_frame.columnconfigure(1, weight=1)

root.mainloop()