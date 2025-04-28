import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = 'https://quotes.toscrape.com'

# Send GET request
response = requests.get(url, timeout=10)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extract quotes and authors
quotes = soup.find_all('div', class_='quote')

data = []

for quote in quotes:
    text = quote.find('span', class_='text').get_text(strip=True)
    author = quote.find('small', class_='author').get_text(strip=True)
    data.append({'Quote': text, 'Author': author})

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('quotes.csv', index=False)

print("✅ Scraping complete! Quotes saved to quotes.csv.")
