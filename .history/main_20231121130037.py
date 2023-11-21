import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding=) as f:
        f.write(r.text)
url= "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url, "data/times.html")