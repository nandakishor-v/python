num=int(input("enter the the number "))
num1=num
sum=0
rem=0
while num1!=0:
          rem=num1%10
          sum=sum+rem*rem*rem
          num1=num1//10
if(num==sum):
          print("amstrong number")
else:
          print("not a amstrong number")

          