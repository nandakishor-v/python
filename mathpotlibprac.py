# importing module
import matplotlib.pyplot as plt

# assigning x and y coordinates
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = []

for i in range(len(x)):
	y.append(max(0, x[i]))

# depicting the visualization
ax = plt.plot(x, y, color='green')

# turn off the axes
#plt.axis('off')

# displaying the title
plt.title("ReLU function graph")

plt.show()
