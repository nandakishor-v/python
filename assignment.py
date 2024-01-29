import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Function to extract article text from a URL
def extract_article_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting article title and text
        title = soup.title.text.strip()
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        return title, article_text
    except Exception as e:
        print(f"Error extracting article from {url}: {e}")
        return None, None

# Read Excel file
excel_file = 'C:\\Users\\nanda\\Downloads\\Input.xlsx'
df = pd.read_excel(excel_file)


# Create a directory to save text files
output_directory = 'output_articles'
os.makedirs(output_directory, exist_ok=True)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Extract article text
    title, article_text = extract_article_text(url)

    # Save article text in a text file
    if title and article_text:
        file_name = f"{url_id}.txt"
        file_path = os.path.join(output_directory, file_name)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n")
            file.write(article_text)

        print(f"Article saved: {file_path}")
