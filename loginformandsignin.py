from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

def login():
    username = username_login_entry.get()
    password = password_login_entry.get()

    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="study"
    )
    cursor = con.cursor()

    cursor.execute("SELECT * FROM form WHERE USERNAME = %s AND PASSWORD = %s", (username, password))
    row = cursor.fetchall()

    if row:
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def export():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = Email_entry.get()
    gender = gender_val.get()
    username = Username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not all([first_name, last_name, email, gender, username, password, confirm_password]):
        messagebox.showerror("Error", "All fields must be filled")
    elif password != confirm_password:
        messagebox.showerror("Error", "Password and Confirm Password do not match")
    else:
        con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="study"
        )
        cursor = con.cursor()

        cursor.execute("SELECT * FROM form WHERE USERNAME = %s", (username,))
        row = cursor.fetchall()

        if not row:
            pattern=r"^[a-zA-Z0-9_+.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if re.match(pattern,email)is not None:
                          
              cursor.execute("INSERT INTO form (FIRST_NAME, LAST_NAME, EMAIL, GENDER, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, email, gender, username, password))
              con.commit()
            else:
                          messagebox.showerror("error","enter email")
            messagebox.showinfo("Info", "Registration successful")
        else:
            messagebox.showerror("Error", "Username already taken")

def switch_to_login():
    signin_pannel.pack_forget()
    login_pannel.pack()

def switch_to_signin():
    login_pannel.pack_forget()
    signin_pannel.pack()



    

root = Tk()
root.title("Registration and Login Form")
root.geometry("500x300")
# Initialize PanedWindows
login_pannel = PanedWindow(root)
signin_pannel = PanedWindow(root)

# Registration Form
'''registration_frame = Frame(root)
registration_frame.grid(row=0, column=0, padx=10, pady=10)'''

first_name_label = Label(signin_pannel, text="First Name:")
first_name_label.grid(row=0, column=0)
first_name_entry = Entry(signin_pannel)
first_name_entry.grid(row=0, column=1)

#last name
last_name_label = Label(signin_pannel,text="Last name ")
last_name_label.grid(row=1,column=0)
last_name_entry=Entry(signin_pannel)
last_name_entry.grid(row=1,column=1)

#Email
Email_label = Label(signin_pannel,text="Email")
Email_label.grid(row=2,column=0)
Email_entry=Entry(signin_pannel)
Email_entry.grid(row=2,column=1)

#radio button

Gender_label = Label(signin_pannel,text="Gender")
Gender_label.grid(row=3,column=0)
gender_val = StringVar()
rb=Radiobutton(signin_pannel,text="Male",variable=gender_val,value="m")
rb.grid(row=3,column=1)
rb1=Radiobutton(signin_pannel,text="Female",variable=gender_val,value="f")
rb1.grid(row=3,column=2)

#Username
Username_label = Label(signin_pannel,text="Username")
Username_label.grid(row=4,column=0)
Username_entry=Entry(signin_pannel)
Username_entry.grid(row=4,column=1)

#Password
password_label = Label(signin_pannel,text="Password")
password_label.grid(row=5,column=0)
password_entry=Entry(signin_pannel,show="*")
password_entry.grid(row=5,column=1)

confirm_password_label = Label(signin_pannel, text="Confirm Password:")
confirm_password_label.grid(row=6, column=0)
confirm_password_entry = Entry(signin_pannel, show="*")
confirm_password_entry.grid(row=6, column=1)

register_button = Button(signin_pannel, text="Register", command=export)
register_button.grid(row=7, column=0, columnspan=2, pady=10)

# Login Form
'''login_frame = Frame(root)
login_frame.grid(row=0, column=1, padx=10, pady=10)'''

#username login
username_login_label = Label(login_pannel, text="Username:")
username_login_label.grid(row=0, column=0)
username_login_entry = Entry(login_pannel)
username_login_entry.grid(row=0, column=1)

#password login
password_login_label = Label(login_pannel, text="Password:")
password_login_label.grid(row=1, column=0)
password_login_entry = Entry(login_pannel, show="*")
password_login_entry.grid(row=1, column=1)

login_button = Button(login_pannel, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons to switch between Registration and Login
switch_to_login_button = Button(root, text="Switch to Login", command=switch_to_login)
switch_to_login_button.pack()

switch_to_signin_button = Button(root, text="Switch to Sign In", command=switch_to_signin)
switch_to_signin_button.pack()



# Initial configuration

root.mainloop()
