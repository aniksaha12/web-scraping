import requests

def fetchAndSave
url= "https://book.spicejet.com/RetrieveBooking.aspx"

r = requests.get(url)
print (r.text)