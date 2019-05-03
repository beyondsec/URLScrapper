from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://target.com/"

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('a'):
    print(link.get('href'))
