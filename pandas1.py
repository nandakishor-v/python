import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''x = [2, 5, 4, 3, 7, 45, 8, 2, 4, 6]
x = pd.Series(x, index=("d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9","d10"))
print(x)

y={
          "name":"kichu",
          "age":21
}

y=pd.Series(y)
print(y)'''

x={
          "name":["hello","hi","kello","ein"],
          "age":[10,30,28,15]
}

x=pd.DataFrame(x)
print(x.loc[1])
