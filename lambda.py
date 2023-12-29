


#lambda function 
def myfuction(n):
          return lambda a: a+n


n=int(input("enter the number "))
a=int(input("Second number "))
my_number=myfuction(n)
print(my_number(a))


#exceptionhandling

def exception(a):
          try:
                    a=a/(a-3)
          except:ZeroDivisionError
          finally:
                    print(a)
          
print(exception(3))
                    
                    



