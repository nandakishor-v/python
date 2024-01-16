from tkinter import *
from tkinter import messagebox

def export():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    # Store the details in a dictionary with the name as the key
    details[name] = {
        "Email": email,
        "Phone": phone,
        "Address": address
    }

    # Display a success message
    messagebox.showinfo("Success", "Adding successful!")

    # Clear the entry fields
    reset()
    name_entry.focus_set()

def reset():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    name_entry.focus_set()

def search():
    # Clear the listbox
    details_listbox.delete(0, END)

    # Get the search query
    search_query = search_entry.get()

    # Display details for the searched name
    if search_query in details:
        details_listbox.insert(END, f"Name: {search_query}")
        details_listbox.insert(END, f"Email: {details[search_query]['Email']}")
        details_listbox.insert(END, f"Phone: {details[search_query]['Phone']}")
        details_listbox.insert(END, f"Address: {details[search_query]['Address']}")
    else:
        details_listbox.insert(END, "Name not found.")


root = Tk()
root.title("Form")
root.geometry("500x500")

details = {}  # Dictionary to store details

name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)


email_label = Label(root, text="Email")
email_label.grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)


phone_label = Label(root, text="Phone")
phone_label.grid(row=2, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=2, column=1)


address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
address_entry = Entry(root)
address_entry.grid(row=3, column=1)


add_button = Button(root, text="Add", command=export)
add_button.grid(row=5, column=1)

reset_button = Button(root, text="Reset", command=reset)
reset_button.grid(row=5, column=2)

search_entry = Entry(root, width=20)
search_entry.grid(row=6, column=1)
search_button = Button(root, text="Search", command=search)
search_button.grid(row=6, column=2)

# Create a listbox to display details
details_listbox = Listbox(root, height=10, width=40)
details_listbox.grid(row=7, column=1, columnspan=2, rowspan=4)

root.mainloop()
