import requests
from bs4 import BeautifulSoup, Tag

url = r'https://www.immobilienscout24.at/expose/6107c16fa909aa001b176a77'

r = requests.get(url, timeout=(3.05, 27))

soup = BeautifulSoup(r.content, 'html.parser')

section = soup.find('section', {'class': 'rxmi5'})
spans = section.find_all('span', recursive=False)


def Convert(lst):
    res_dct = {
        lst[i].get_text():
            lst[i + 1].get_text() for i in range(0, len(lst), 2)
        }
    return res_dct


dict = Convert(spans)
print(dict)
