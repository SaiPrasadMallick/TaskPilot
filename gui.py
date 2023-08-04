import tkinter as tk
from tkinter import messagebox
from task_manager import signup, login

def handle_signup():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        signup()
        messagebox.showinfo("Success", "Sign up successful! Please proceed to log in.")
        root.destroy()
    else:
        messagebox.showerror("Error", "Please enter a valid username and password.")

def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        login()
        root.destroy()
    else:
        messagebox.showerror("Error", "Please enter a valid username and password.")

root = tk.Tk()
root.title("TaskPilot - Personal Task Manager")
root.geometry("400x300")

label = tk.Label(root, text="WELCOME TO TaskPilot, your Personal TASK MANAGER")
label.pack()

label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root, width=30)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

signup_button = tk.Button(root, text="Sign Up", command=handle_signup)
signup_button.pack()

login_button = tk.Button(root, text="Log In", command=handle_login)
login_button.pack()

root.mainloop()
