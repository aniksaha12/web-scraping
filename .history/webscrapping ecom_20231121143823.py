import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}
   
url= "https://www.amazon.in/s?k=iphone&crid=1HDFNSMWVLXSE&sprefix=iphone%2Caps%2C231&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, proxies=proxies, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

spans = soup.find(class = "")

