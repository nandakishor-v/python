import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import StringVar, messagebox

def export():
    print(lan.get())
    print(gender.get())
  #  print(li.curselection())
    
    
def click():
              r=Toplevel(p1)
          
windows=Tk()

#label
username=Label(windows,text="username",font="Modern 20 bold",bg="red",fg="yellow",height="1",width="10")
username.pack()

#image
img = ImageTk.PhotoImage(Image.open("calc.png"))
label=Label(windows,image=img,height="300",width="400")
label.pack()

entry=Entry(windows,text="username",bg="black",fg="white")
entry.pack()

#button
b = Button(windows,text="submit",activebackground="black",activeforeground="green",command=export)
b.pack()

#check button
lan= StringVar()
b1=Checkbutton(windows,text="English",variable=lan, onvalue="en", offvalue="null")
b1.pack()

#radio button
gender = StringVar()
rb=Radiobutton(windows,text="Male",variable=gender,value="m")
rb.pack()
rb1=Radiobutton(windows,text="Female",variable=gender,value="f")
rb1.pack()


'''
#scrollbar in list box
yscrollbar=Scrollbar(windows)
yscrollbar.pack(side=RIGHT,fill=Y)

xscrollbar=Scrollbar(windows)
xscrollbar.pack(side=BOTTOM,fill=X)

#listbox
li=Listbox(windows,selectmode=MULTIPLE,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
for line in range(100):
          li.insert(END,"line is  "+str(line))
li.pack()
yscrollbar.config(command=li.yview)
xscrollbar.config(command=li.xview)'''

#panelwindow
p=PanedWindow(windows,bg="red",width=100,height=100)
p.pack(side=RIGHT)

p1=PanedWindow(windows,bg="yellow",width=100,height=100)
p1.pack(side=LEFT)

p2=PanedWindow(windows,bg="black",width=100,height=100)
p2.pack(side=TOP)

p3=PanedWindow(windows,bg="blue",width=100,height=100)
p3.pack(side=BOTTOM)

b1=Button(p1,text="hello",command=click)
b1.grid(row=0,column=0)


windows.iconphoto(False,img)
windows.title("simpleGui")
windows.geometry("1400x1400")
windows.mainloop()