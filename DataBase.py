import tkinter as tk

# Define the window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x200")

# Define the labels and text entry fields
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


# Define the login button and function
def login():
    # Validate the username and password
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        # Open the main menu
        main_menu()
    else:
        # Display an error message
        error_label.config(text="Invalid username or password")


login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

error_label = tk.Label(root, fg="red")
error_label.pack()


# Define the main menu function
def main_menu():
    # Create the main menu window
    main_window = tk.Toplevel(root)
    main_window.title("Main Menu")
    main_window.geometry("400x400")

    # Add buttons for different tasks
    view_students_button = tk.Button(main_window, text="View Students")
    view_students_button.pack()

    add_student_button = tk.Button(main_window, text="Add Student")
    add_student_button.pack()

    view_reports_button = tk.Button(main_window, text="View Reports")
    view_reports_button.pack()


# Start the main event loop
root.mainloop()
