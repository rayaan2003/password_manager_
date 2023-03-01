import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Password Storing Application")

# Add a label for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Add a button to store the password
def store_password():
    username = username_entry.get()
    password = password_entry.get()
    # Code to store the password goes here
    print(f"Stored {username}'s password: {password}")

store_button = tk.Button(root, text="Store Password", command=store_password)
store_button.pack()

# Run the window
root.mainloop()
