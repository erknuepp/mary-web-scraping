from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
response = s.get('https://www.immobilienscout24.at/regional/wien/wien/wohnung-mieten')
response.html.render()

print(response)

soup = BeautifulSoup(response.content, 'html.parser')

# get all links of the new appartments
results = soup.find_all('li', {'class': 'sYBBf'})
print(results)