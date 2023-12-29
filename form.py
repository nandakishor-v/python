from tkinter import *
from tkinter import messagebox
import mysql.connector


def Login():
        r=Toplevel(loginpannel)     
        Username=Username_entry.get()
        password=password_entry.get()
            
#export and checking if the field is empty or not
def export():
          r=Toplevel(signinpannel)
          first_name =first_name_entry.get()
          last_name =last_name_entry.get()
          Email =Email_entry.get()
          gender=gender_val.get()
          Username=Username_entry.get()
          password=password_entry.get()
          Confirmpassword=Confirmpassword_entry.get()
          
          if first_name=="":
                        messagebox.showerror("error","first name field is empty")
          elif last_name=="":
                        messagebox.showerror("error","last name field is empty")
          elif Email=="":
                        messagebox.showerror("error","Email field is empty")
          elif gender=="":
                        messagebox.showerror("error","gender field is empty")
          elif Username=="":
                      messagebox.showerror("error","username is empty")
          elif password=="":
                      messagebox.showerror("error","password is empty")
          elif Confirmpassword=="" or password!=Confirmpassword:
                      messagebox.showerror("error","empty field or password is not same ")
                        
          else:    #sql connection            
           ''' print(first_name)
            print(last_name)
            print(Email)
            print(gender)
            print(Username)
            print(password)'''
           con=mysql.connector.connect(
             host="127.0.0.1",
             user="root",
             password="",
             database="study"
           )
           cursor =con.cursor()
           
           cursor.execute("SELECT * FROM form WHERE USERNAME =%s",(Username,))
           row =cursor.fetchall()
           print(row)
           if not row:
                       cursor.execute("INSERT INTO form (FIRST_NAME,LAST_NAME,EMAIL,GENDER,USERNAME,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s)",(first_name,last_name,Email,gender,Username,password))
                       con.commit()
                       messagebox.showinfo("info","value inserted")
           else:
                       messagebox.showerror("error","username already taken")
                      
                       
            
            
            
          

root = Tk()
root.title("Registration Form")
root.geometry("300x300")

#first name
first_name_label = Label(root,text="First name ")
first_name_label.grid(row=0,column=0)
first_name_entry=Entry(root)
first_name_entry.grid(row=0,column=1)

#last name
last_name_label = Label(root,text="Last name ")
last_name_label.grid(row=1,column=0)
last_name_entry=Entry(root)
last_name_entry.grid(row=1,column=1)

#Email
Email_label = Label(root,text="Email")
Email_label.grid(row=2,column=0)
Email_entry=Entry(root)
Email_entry.grid(row=2,column=1)

#radio button

Gender_label = Label(root,text="Gender")
Gender_label.grid(row=3,column=0)
gender_val = StringVar()
rb=Radiobutton(root,text="Male",variable=gender_val,value="m")
rb.grid(row=3,column=1)
rb1=Radiobutton(root,text="Female",variable=gender_val,value="f")
rb1.grid(row=3,column=2)

#Username
Username_label = Label(root,text="Username")
Username_label.grid(row=4,column=0)
Username_entry=Entry(root)
Username_entry.grid(row=4,column=1)

#Password
password_label = Label(root,text="Password")
password_label.grid(row=5,column=0)
password_entry=Entry(root,show="*")
password_entry.grid(row=5,column=1)

#Confirm Password
Confirmpassword_label = Label(root,text="Confirm Password")
Confirmpassword_label.grid(row=6,column=0)
Confirmpassword_entry=Entry(root,show="*")
Confirmpassword_entry.grid(row=6,column=1)



#button
b = Button(root,text="submit",activebackground="black",activeforeground="green",command=export)
b.grid(row=7,column=0,)




#pannel window
loginpannel=PanedWindow(root)
loginpannel.grid(row=0,column=0)

signinpannel=PanedWindow(root)
signinpannel.grid(row=0,column=1)

loginbutton=Button(loginpannel,text="login",command=Login)
signinbutton=Button(signinpannel,text="sign in",command=export)


root.mainloop()


       

