from tkinter import *

def km():
    print(kilonumber1_entry.get())
    print(int(kilonumber1_entry.get()) * 1000)

def m():
    print(int(meternumber1_entry.get()) / 1000)

def c():
    print((int(degreenumber1_entry.get()) * 1.8) + 32)

def f():
    print((int(farhnumber1_entry.get()) - 32) * (5 / 9))

def switch_to_kilo():
    meterpannel.pack_forget()
    degreepannel.pack_forget()
    farhnpannel.pack_forget()
    kilometerpannel.pack()

def switch_to_meter():
    kilometerpannel.pack_forget()
    degreepannel.pack_forget()
    farhnpannel.pack_forget()
    meterpannel.pack()

def switch_to_degree():
    kilometerpannel.pack_forget()
    farhnpannel.pack_forget()
    meterpannel.pack_forget()
    degreepannel.pack()

def switch_to_farh():
    kilometerpannel.pack_forget()
    degreepannel.pack_forget()
    meterpannel.pack_forget()
    farhnpannel.pack()

root = Tk()
root.title("Converter")
root.geometry("300x300")

# Pannel window
kilometerpannel = PanedWindow(root)
meterpannel = PanedWindow(root)
degreepannel = PanedWindow(root)
farhnpannel = PanedWindow(root)

# Kilometer
kilonumber1_lable = Label(kilometerpannel, text="enter the Km")
kilonumber1_lable.grid(row=0, column=0)
kilonumber1_entry = Entry(kilometerpannel)
kilonumber1_entry.grid(row=0, column=1)
convert_button = Button(kilometerpannel, text="convert", command=km)
convert_button.grid(row=7, column=0, columnspan=2, pady=10)

# Meter
meternumber1_lable = Label(meterpannel, text="enter the M")
meternumber1_lable.grid(row=0, column=0)
meternumber1_entry = Entry(meterpannel)
meternumber1_entry.grid(row=0, column=1)
convert_button = Button(meterpannel, text="convert", command=m)
convert_button.grid(row=7, column=0, columnspan=2, pady=10)

# Degree
degreenumber1_lable = Label(degreepannel, text="enter the c")
degreenumber1_lable.grid(row=0, column=0)
degreenumber1_entry = Entry(degreepannel)
degreenumber1_entry.grid(row=0, column=1)
convert_button = Button(degreepannel, text="convert", command=c)
convert_button.grid(row=7, column=0, columnspan=2, pady=10)

# Farh
farhnumber1_lable = Label(farhnpannel, text="enter the f")
farhnumber1_lable.grid(row=0, column=0)
farhnumber1_entry = Entry(farhnpannel)
farhnumber1_entry.grid(row=0, column=1)
convert_button = Button(farhnpannel, text="convert", command=f)
convert_button.grid(row=7, column=0, columnspan=2, pady=10)

switch_to_kilo_button = Button(root, text="Switch to km", command=switch_to_kilo)
switch_to_kilo_button.pack()

switch_to_meter_button = Button(root, text="Switch to M", command=switch_to_meter)
switch_to_meter_button.pack()

switch_to_degree_button = Button(root, text="Switch to c", command=switch_to_degree)
switch_to_degree_button.pack()

switch_to_farh_button = Button(root, text="Switch to f", command=switch_to_farh)
switch_to_farh_button.pack()

root.mainloop()
