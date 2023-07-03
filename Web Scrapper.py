import requests
import re
from bs4 import BeautifulSoup

# URL of the product page
url = 'https://www.amazon.in/realme-Storage-Dimensity-Processor-Display/dp/B09ZBFD6TJ/ref=sr_1_1?keywords=realme%2Bnarzo%2B50%2Bpro%2B5g&qid=1679110788&sprefix=realme%2Bnar%2Caps%2C228&sr=8-1&th=1'

# Sending a request to the URL and retrieve the HTML content
response = requests.get(url)
content = response.content

# Parsing the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find the element containing the price of the product
element = soup.find('span', {'class': 'a-price-whole'})

# Extract the price value from the element

if element is not None:
    text = element.text
    print(text)
else:
    print('Element not found')