def fact(num):
          fac=1
          for i in range(2,num+1):
                    fac *=i
          return fac

num=int(input("enter the number"))
temp=num
rem=0
b=0
while num!=0:
          rem=num%10
         
          b+=fact(rem)
          num=num//10
          
if b==temp:
          print(f"{temp} is a strong number")
else:
          print(f"{temp} not a strong number")
          
          
          
