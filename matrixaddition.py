import numpy as np

def rmatrix(row,col):
          matrix=[]
          for i in range(row):
                    r=[int(num)for num in input(f"Enter the value of row {i}: ").split()]
                    if len(r)!=col:
                           raise ValueError("values exceeds the number of column ")
                    matrix.append(r)
          return matrix


row=int(input("Enter the number of rows "))
col=int(input("Enter the number of column "))

matrix_a= rmatrix(row,col)
matrix_b= rmatrix(row,col)

print(matrix_a)
print(matrix_b)

choice=int(input("Enter the your choice 1:Add 2:sub 3:div 4:mult (enter the number ) "))
if choice==1:
           result=np.add(matrix_a,matrix_b)
           print(result)
elif choice==2:
           result=np.subtract(matrix_a,matrix_b)
           print(result)
elif choice==3:
           result=np.divide(matrix_a,matrix_b)
           print(result)
else:
      result=np.multiply(matrix_a,matrix_b)
      print(result)

                    
                    
