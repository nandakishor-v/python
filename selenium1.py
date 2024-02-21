from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

try:
    # Open the URL in the browser
    driver.get(url)

    # Wait for the page to load (you can adjust the sleep time if needed)
    driver.implicitly_wait(5)

    # Get the page source after waiting
    page = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table')

    # Check if there is at least one table
    if tables:
        # Extract the first table
        first_table = tables[1]

        # Extract the table rows
        rows = first_table.find_all('tr')

        # Check if there are rows in the table
        if len(rows) > 0:
            # Extract the column headers
            header = [th.text.strip() for th in rows[0].find_all('th')]

            # Initialize an empty list to store the data
            data = []

            # Iterate over the remaining rows and extract the data
            for row in rows[1:]:
                row_data = [td.text.strip() for td in row.find_all('td')]
                data.append(row_data)

            # Create a DataFrame
            df = pd.DataFrame(data, columns=header)

            # Display the DataFrame
            print(df)
        else:
            print("No rows found in the HTML table.")
    else:
        print("No tables found on the page.")
        


finally:
    # Close the webdriver
    driver.quit()
    df.to_csv("csvfiles.csv")
