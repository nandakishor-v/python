import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_rows = 1100
df = pd.read_excel('Bike Purchased.xlsx')

# Drop duplicates
newdf = df.drop_duplicates()

# Replace values in the 'Gender' column
newdf['Gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)

# Replace values in the 'Marital Status' column
newdf['Marital Status'].replace({'M': 'Married', 'S': 'Single'}, inplace=True)

# Drop columns
newdf.drop(['Cars', 'Commute Distance', 'Children', 'Education', 'Home Owner'], axis=1, inplace=True)

# Categorize 'Age' based on conditions
conditions = [
    (newdf['Age'] > 50),
    (newdf['Age'] > 30),
    (newdf['Age'] > 18)
]
choices = ['old', 'middle', 'young']

# Assign the result back to the 'Age' column
newdf['Age'] = np.select(conditions, choices, default=newdf['Age'])

# Filter data where 'Purchased Bike' is 'Yes'
bike_purchased_yes = newdf[newdf['Purchased Bike'] == 'Yes']

# Creating subplots for bar chart and pie chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart
grouped_data = newdf.groupby(['Region', 'Gender', 'Purchased Bike']).size().unstack()
grouped_data.plot(kind='bar', ax=ax1)
ax1.set_title('Number of Bike Buyers in Different Regions by Gender')
ax1.set_xlabel('Region')
ax1.set_ylabel('Number of Buyers')
ax1.legend(title='Gender')

# Pie chart
gender_counts = bike_purchased_yes['Gender'].value_counts()
gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax2)
ax2.set_title('Distribution of Bike Buyers by Gender (Purchased Bike = Yes)')

# Display the plot
plt.show()
