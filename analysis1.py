import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 101

df = pd.read_csv("csvfiles.csv")
df.drop(['Unnamed: 0', 'Rank', 'Headquarters'], axis=1, inplace=True)
newdf = df.drop_duplicates()

newdf['Name'] = newdf['Name'].str.title()
newdf['Name'] = newdf['Name'].str.strip()
newdf['Revenue growth'] = pd.to_numeric(newdf['Revenue growth'].str.strip('%'), errors='coerce')

# Replace commas with an empty string and then convert to numeric
newdf['Revenue (USD millions)'] = pd.to_numeric(newdf['Revenue (USD millions)'].str.replace(',', ''), errors='coerce')

newdf['Industry'] = newdf['Industry'].str.strip()

# Assuming you want to plot the count of companies in each industry
industry_counts = newdf['Industry'].value_counts()

# Plotting the bar plot for count of companies in each industry
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
industry_counts.plot(kind='bar', ax=ax1)
ax1.set_title('Number of Companies in Each Industry')
ax1.set_xlabel('Industry')
ax1.set_ylabel('Count')

# Grouped bar plot for 'Revenue growth' and 'Revenue (USD millions)' within each industry
grouped_data = newdf.groupby('Industry')[['Revenue growth', 'Revenue (USD millions)']].mean()
grouped_data.plot(kind='bar', ax=ax2)
ax2.set_title('Average Revenue Growth and Revenue within Each Industry')
ax2.set_xlabel('Industry')
ax2.set_ylabel('Average Values')  # Update y-axis label

plt.show()

print(newdf)
