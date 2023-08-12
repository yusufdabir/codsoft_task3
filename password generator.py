import tkinter as tk
import string
import random

def generate_password():
    username = username_entry.get()
    password_length = int(length_entry.get())

    if username and password_length > 0:
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))

        generated_password_label.config(text=f"Generated Password: {generated_password}")
    else:
        generated_password_label.config(text="Please enter a valid username and password length.")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_label.config(text="")
    status_label.config(text="")

def accept_password():
    accepted_password = generated_password_label.cget("text").replace("Generated Password: ", "")
    # You can do something with the accepted_password, e.g., store it in a file or a database.
    status_label.config(text="Password saved successfully.")

# Main GUI window
root = tk.Tk()
root.title("Password Generator")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

username_label = tk.Label(input_frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(input_frame, width=30)
username_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = tk.Label(input_frame, text="Password Length:")
length_label.grid(row=1, column=0, padx=5, pady=5)

length_entry = tk.Entry(input_frame, width=30)
length_entry.grid(row=1, column=1, padx=5, pady=5)

# Generate, Accept, and Reset buttons
generate_button = tk.Button(input_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=1, padx=5, pady=10)

accept_button = tk.Button(input_frame, text="Accept Password", command=accept_password)
accept_button.grid(row=3, column=1, padx=5, pady=10)

reset_button = tk.Button(input_frame, text="Reset", command=reset_fields)
reset_button.grid(row=4, column=1, columnspan=2, padx=5, pady=10)

# Output frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

generated_password_label = tk.Label(output_frame, text="", font=("Arial", 12))
generated_password_label.pack()

# Status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Run the GUI main loop
root.mainloop()
