# import required modules 
import matplotlib.pyplot as plt 
import numpy as np 
	
# time series data 
geeksx = np.array([24.40, 110.25, 20.05, 
				22.00, 61.90, 7.80, 
				15.00]) 

geeksy = np.array([24.40, 110.25, 20.05, 
				22.00, 61.90, 7.80, 
				15.00]) 
	
# depict illustration 
fig, ax = plt.subplots() 
ax.xcorr(geeksx, geeksy, maxlags = 6, 
		color ="green") 

# turn off the axes
ax.set_axis_off() 

# assign title
ax.set_title('Time series graph') 
plt.show() 
