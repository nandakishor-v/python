import pandas as pd
import numpy as np

def solutionq(a,b,c):
          discriment=np.sqrt((b**2)-(4*a*c))
          if discriment>0:
                    root1=(-b+discriment)/(2*a)
                    root2=(-b-discriment)/(2*a)
                    return root1,root2
          elif discriment==0:
                    root=-b/(2*a)
                    return root
          else:
                    print("the equation has zero real solutions ")
                    
          

a=float(input("coefficant of a "))
b=float(input("coefficant of b "))
c=float(input("coefficant of c "))

print(f"The equation is {a}x^2 + {b}x + {c}")

root=solutionq(a,b,c)
print(f"the roots are {root}")




