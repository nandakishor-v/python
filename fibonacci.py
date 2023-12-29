limt = int(input("Enter the limit "))
'''n1=0
n2=1
n3=0
print(n1,n2,end=" ")
for i in range(2,limt+1):
          n3=n1+n2
          print(n3,end=" ")
          n1=n2
          n2=n3'''
          
def fibonaci(num):
          if num==0 or num ==1:
                    return num
          else :
                    return fibonaci(num-1)+fibonaci(num-2)
          
for i in range(0,limt):
          print(fibonaci(i),end=" ")
          