import json
import requests


def random_brew():

    try:

        # simple request to fetch and display data from an api #
        url = "https://api.openbrewerydb.org/v1/breweries/randoms"
        response = requests.get(url)
        print("http status code: ",  response.status_code, "\n")
        response.raise_for_status()
        # parses JSON string and converts into a Python dictionary
        # json_data = json.loads(response.text)
        json_data = response.json()
        print(json_data)

    except requests.exceptions.RequestException as e:
        print("Error:", {e})


random_brew()
