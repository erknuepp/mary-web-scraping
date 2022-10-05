import requests
from bs4 import BeautifulSoup

url = r'https://www.immobilienscout24.at/regional/wien/wien/wohnung-mieten'

r = requests.get(url, timeout=(3.05, 27))

print(r)

soup = BeautifulSoup(r.content, 'html.parser')

# get all links of the new appartments
results = soup.find_all('li', {'class': 'sYBBf'})
print(results)