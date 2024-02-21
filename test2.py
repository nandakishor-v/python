import pandas as pd

pd.options.display.max_rows = 1100
df = pd.read_excel('Data Cleaning Excel Tutorial (1).xlsx')

# Drop duplicates
newdf = df.drop_duplicates()
newdf.drop(['Unnamed: 0', 'prior'], axis=1, inplace=True)

# Use the .str accessor and title() function to capitalize the first letter of each word
newdf['president'] = newdf['president'].str.title()

# Replace values in the 'party' column
newdf['party'].replace({'Whig   April 4, 1841  â€“  September 13, 1841': 'Whig', 'Republicans': 'Republican', 'Demorcatic': 'Democratic','Democratic-  Republican':'Republican'}, inplace=True)

newdf['vice'] = newdf['vice'].str.strip()
newdf['president'] = newdf['president'].str.strip()

# Sort the DataFrame based on the 'party' field
newdf = newdf.sort_values(by='party', ascending=False)

print(newdf)
