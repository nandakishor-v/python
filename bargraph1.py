import numpy as np
import matplotlib.pyplot as ply

x=np.array(["messi","cr7","neymar","xavi"])
y=np.array([500,450,300,400])

ply.subplot(2,2,1)
ply.bar(x,y,color="red")

ply.subplot(2,2,2)
ply.barh(x,y)



ply.subplot(2,2,3)
ply.pie(y,labels=x,shadow=True,explode=[0.1,0,0,0],autopct="%1.1f%%")
ply.legend(title="footballers",loc=(-0.7,0.1))


data=[]
for x in range(100):
          data.append(np.random.rand())


ply.subplot(2,2,4)
ply.hist(data,color="red")

ply.show()

print(np.mean(y))
print(np.median(y))

print(np.var(data))
print(np.std(data))
print(np.percentile(data,1))
