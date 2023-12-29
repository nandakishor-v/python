class person:
          name=""
          age=0
          def __init__(self,name,age):
                    self.name=name
                    self.age=age #constructors
                    
          '''  def details(self,name,age):
                    name.self=name
                    age.self=age'''
                    
          def print1(self):
                print(f"name is {self.name} and age is {self.age}")
                
             
             
a=input("Enter the name ")
b= int (input("enter the age "))  
p1=person(a,b)
p1.print1()
                    
                    
        