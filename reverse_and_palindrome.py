num=int(input("enter the the number "))
num1=num
rev=0
rem=0
while num1!=0:
          rem=num1%10
          rev=rev*10+rem
          num1=num1//10
print(rev)
if num == rev:
          print("it is a palindrome")
else:
          print ("not a palindrom")