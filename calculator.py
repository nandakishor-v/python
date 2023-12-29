from tkinter import *

expression = ""

def btnclick(v):
    global expression
    if v == "=":
        try:
            result = str(eval(expression))
            e.set(result)
        except:
            e.set("Error")
    elif v == 'c':
        expression = ""
        e.set("")
    else:
        expression += str(v)
        e.set(expression)

root = Tk()
root.title("Calculator")

# Display box
e = StringVar()
dispay_enter = Entry(root, textvariable=e, width=30, bd=10)
dispay_enter.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'c', '=', '+'
]
row_val = 1
col_val = 0

for button in buttons:
    Button(root, text=button, command=lambda b=button: btnclick(b), width=5).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.geometry("300x300")
root.mainloop()
