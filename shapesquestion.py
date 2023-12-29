class square:
          def area(self,s):
                    print(s*s)
          def perimeter(self,s):
                    print(4*s)
class traingle:
          def area(self,b,h):
                    print(0.5*b*h)
          def perimeter(self,l,b,h):
                    print(l+b+h)
choice=int(input("enter the choice "))
if(choice==1):
          s=int(input("enter the side lenght "))
          s1=square()
          s1.area(s)
          s1.perimeter(s)
elif(choice==2):
          l=int(input("enter the lenght "))
          b=int(input("enter the base "))
          h=int(input("rnter the height "))
          s2=traingle()
          s2.area(b,h)
          s2.perimeter(l,b,h)
else:
          print("wrong choice pls choice 1 or 2")
                    