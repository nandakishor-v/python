import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# URL to scrape
url = "https://www.scrapethissite.com/pages/forms/"

driver = webdriver.Chrome() 
driver.get(url)


# Get the updated HTML content after JavaScript execution
html_content = driver.page_source

# Parse the HTML table using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the table rows
rows = soup.find_all('tr')

# Check if there are rows in the table
if len(rows) > 0:
    # Extract the column headers
    headers = [th.text.strip() for th in rows[0].find_all('th')]

    # Initialize an empty list to store the data
    data = []

    # Iterate over the remaining rows and extract the data
    for row in rows[1:]:
        row_data = [td.text.strip() for td in row.find_all('td')]
        data.append(row_data)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Display the DataFrame
    print(df)
else:
    print("No rows found in the HTML table.")

# Close the Selenium webdriver
driver.quit()
