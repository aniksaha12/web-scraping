import requests

proxies = {
    # "http": "http://10.10.1.10:3128", 
    # "http": "http://10.10.1.10:1080",
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777',
    'http': 'http:customer-rcodewithharry:ActcitXccRBxbxs@pr.oxylabs.io:7777'
}

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
url= "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url, "data/times.html")