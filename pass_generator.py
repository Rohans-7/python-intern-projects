import random
import string
import tkinter as tk

def generate_password(length):
    """Generates a random password of a given length."""
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use the random module to generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def generate_password_button_clicked():
    """Called when the 'Generate Password' button is clicked."""
    # Get the desired length of the password from the entry field
    length = int(length_entry.get())
    
    # Generate a random password
    password = generate_password(length)
    
    # Display the password in the label
    password_label.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create the widgets
length_label = tk.Label(root, text="Length:")
length_entry = tk.Entry(root)
generate_password_button = tk.Button(root, text="Generate Password", command=generate_password_button_clicked)
password_label = tk.Label(root, text="")

# Add the widgets to the window
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)
generate_password_button.grid(row=1, column=0, columnspan=2)
password_label.grid(row=2, column=0, columnspan=2)

# Run the main loop
root.mainloop()
