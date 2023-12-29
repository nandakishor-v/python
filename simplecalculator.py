def add(num1,num2):
          return num1+num2
def sub(num1,num2):
          return num1-num2
def multi(num1,num2):
          return num1*num2
def div (num1,num2):
          return num1/num2

x=int(input("enter the first number "))
y=int(input("Enter the second number "))
print("1= +, 2= -, 3= *, 4= /")
z=int(input("enter the choice "))
if(z==1):
         print( add(x,y))
elif(z==2):
          print(sub(x,y))
elif(z==3):
          print(multi(x,y))
elif(z==4):
          print(div(x,y))
else:
          
                    print("choose from 1 to 4 ")
                    