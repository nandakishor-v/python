import pandas as pd
pd.options.display.max_rows=200
x=pd.read_csv("people-100.csv")
print(x.head(15))
print(x.info())
m=x["Index"].mean()
x["Index"].fillna(m,inplace=True)
print(x)