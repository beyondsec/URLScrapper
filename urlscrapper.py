from bs4 import BeautifulSoup, SoupStrainer
import requests
import argparse

parser = argparse.ArgumentParser(prog="Web URL Scrapper", usage="Parse all URLs on a given webpage.",description="Provide the link with -u/--url.")


parser.add_argument("-u", "--url", dest="url", required=True, help="url of the target")

url = parser.parse_args().url

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, "lxml")

for link in soup.find_all('a'):
    print(link.get('href'))
