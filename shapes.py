class shapes:
          __name="hfhfhfgh "
          def area(self):
                    print("area")
          def perimeter (self):
                    print("perimeter")
          def getname(self):
                   return self.__name
class square(shapes):
          def area(self):
                    super().area()
                    print("s*s")
          def perimeter(self):
                    super().perimeter()
                    print("4*s")
class traingle(shapes):
          def area(self):
                    super().area()
                    print("0.5*h*b")
          def perimeter(self):
                   super().perimeter()
                   print("a+b+c")
        
        
s=square()
s.area()
print(s.getname())