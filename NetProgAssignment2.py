import json
import requests

print("Hola Amigo")

# simple request to fetch and display data from an api #
url = "https://api.openbrewerydb.org/v1/breweries/random"
response = requests.get(url)
data = response.json()
print(data)
