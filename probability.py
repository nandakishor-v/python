import numpy as np
import seaborn as sb
import matplotlib.pyplot as ply

x= np.random.exponential(size=1000)

sb.distplot(x,hist=False)


ply.show()