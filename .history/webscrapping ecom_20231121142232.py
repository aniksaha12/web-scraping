import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}

def fetchAndSaveToFile(url, path):
    r = requests.get(url, proxies=proxies)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
url= "https://www.spicejet.com/"

fetchAndSaveToFile(url, "data/times.html")

soup = BeautifulSoup(html_doc, "html.parser")