# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Set display options for Pandas DataFrame
pd.options.display.max_rows = 200

# Read the CSV file into a Pandas DataFrame
x = pd.read_csv("data.csv")

# Calculate the mean of the "Calories" column and fill missing values with the mean
m = x["Calories"].mean()
x["Calories"] = x["Calories"].fillna(m)

# Check for and print duplicated rows in the DataFrame
print(x.duplicated())

# Remove duplicate rows in the DataFrame in place
x.drop_duplicates(inplace=True)

# Check for and print duplicated rows again after removal
print(x.duplicated())

# Calculate and print the correlation matrix for all columns in the DataFrame
print(x.corr())

# Plot the entire DataFrame (assuming you have numeric columns for plotting)
x.plot()

# Create a scatter plot of "Duration" vs. "Calories"
x.plot(kind="scatter", x='Duration', y='Calories')

# Display the plots
plt.show()
