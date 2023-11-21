import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
url= "https://book.spicejet.com/RetrieveBooking.aspx"

fetchAndSaveToFile(url, "data/spicejet.html")