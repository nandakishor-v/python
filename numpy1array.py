import numpy as np
from numpy import *

'''a = np.array([1, 2, 3, 4, 5, 6])
print(a)

b = np.array([[2, 3, 4], [4, 6, 7]])
print(b)

c=np.array([[[45,3,5],[5,7,2]],[[5,6,7],[4,7,8]]])
print(c)
'''
'''print(a[1:3:2])

print(b[1,1])

print(a.dtype)
d=a.copy()
a[0]=34
e=a.view()
print(a)
print(d)
print(e) '''

'''
print(a.shape)
print(a.size)
print(b.shape)
print(b.reshape(3,2,1))
print(b.size)'''

'''for x in nditer(a):
          print(x)
          
for x in nditer(b,flags=['buffered'],op_dtypes=['S']):
          print(x)
          
for x in nditer(c[:,::2]):
          print(x)
          
for idx,x in ndenumerate(c):
          print(idx,x)'''
          
a=array([1,2,3,4])
a1=array([5,6,7,8])

print(concatenate([a,a1]))


b=array([[1,2],[3,4]])
b1=array([[6,7],[8,9]])
print(concatenate([b,b1]))
print(concatenate([b,b1],axis=1))

print(stack((a,a1)))
print(hstack((a,a1)))
print(vstack((a,a1)))
print(dstack((a,a1)))

