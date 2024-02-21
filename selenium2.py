from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.scrapethissite.com/pages/ajax-javascript/#2013"

driver = webdriver.Chrome()
driver.get(url)

# Wait for the loading spinner to disappear
wait = WebDriverWait(driver, 5)
wait.until(EC.invisibility_of_element_located((By.ID, 'loading')))

# Get the updated page source after waiting for the dynamic content
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

body = soup.find('tbody')
rows = body.find_all('tr')

heading = [th.text.strip() for th in soup.find('thead').find_all('th')]
data = []

for row in rows:
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

df = pd.DataFrame(data, columns=heading)

# Drop the 'Best Picture' column
newdf = df.drop(['Best Picture'], axis=1)

# Convert 'Nominations' and 'Awards' columns to numeric
newdf['Nominations'] = pd.to_numeric(newdf['Nominations'])
newdf['Awards'] = pd.to_numeric(newdf['Awards'])

# Plotting
fig, ax = plt.subplots(figsize=(15, 10))

# Group by 'Title' and plot 'Nominations' and 'Awards' as horizontal bars
grouped_df = newdf.groupby('Title')[['Nominations', 'Awards']].sum()
grouped_df.plot(kind='barh', ax=ax)

# Adding annotations (numbers) above the bars
for index, value in enumerate(grouped_df['Nominations']):
    plt.text(value, index, str(value), ha='center', va='center', fontweight='bold')

for index, value in enumerate(grouped_df['Awards']):
    plt.text(value, index, str(value), ha='center', va='center', fontweight='bold')

plt.title('Nominations and Awards by Title')
plt.xlabel('Count')
plt.ylabel('Title')

plt.show()

# Close the browser window
driver.quit()
