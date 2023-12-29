num=int(input("enter the number "))



'''if num == 0:
          print(f"{num}! is 1")
else:
                   
          fact = 1
          for i in range(2,num+1):
           fact *=i
          print(f"{num}! is {fact}")'''


def fact(num):
          fac=1
          for i in range(2,num+1):
                    fac *=i
          return fac

print(fact(num))
