class student:
          def name(self,name,age):
                    self.name=name
                    self.age=age
                    print(f"{self.name} and {self.age}")
class parent:
          def print1(self):
                    print("parent ")
class teacher(parent,student):
          def print1(self):
                    print("teacher")
class admin(teacher):
          def print1(self):
                    super().print1()
                    print("admin")
                    
                    
s=admin()
s.print1()
                    