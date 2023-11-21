import requests

def fetchand
url= "https://book.spicejet.com/RetrieveBooking.aspx"

r = requests.get(url)
print (r.text)