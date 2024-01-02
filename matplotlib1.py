import matplotlib.pyplot as ply
import numpy as np

x=np.array([1,1,3,3])
y=np.array([7,5,5,3])
ply.subplot(2,2,1)
ply.plot(x,y)


x1=np.array([3,2,2,1])
y1=np.array([7,7,3,3])
ply.subplot(2,2,2)
ply.plot(x1,y1)

x2=np.array([1.5])
y2=np.array([6])

x3=np.array([1.5])
y3=np.array([4])

x4=np.array([2.5])
y4=np.array([6])

x5=np.array([2.5])
y5=np.array([4])

ply.plot(x,y,marker="o",c="red",linestyle="dotted",linewidth=3)
ply.plot(x1,y1,marker="*",linestyle="dashed",linewidth=3)
ply.plot(x2,y2,marker="o")
ply.plot(x3,y3,marker="o")
ply.plot(x4,y4,marker="o")
ply.plot(x5,y5,marker="o")
ply.title("Logo",fontdict={"family":"times new roman","color":"purple","size":30})
ply.xlabel("blue")
ply.ylabel("red")
ply.grid(color="green")
ply.show()