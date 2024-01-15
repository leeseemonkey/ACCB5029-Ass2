import json
import requests
import pprint


def random_brew():

    try:

        # simple request to fetch and display data from an api #
        url = "https://api.openbrewerydb.org/v1/breweries/random"
        response = requests.get(url)
        print("http status code: ",  response.status_code, "\n")
        response.raise_for_status()
        # parses JSON string and converts into a Python dictionary
        # json_data = json.loads(response.text)
        json_data = response.json()
        print("Unformatted JSON data:", json_data, "\n")

        print("As a Python dictionary", json_data[0], "\n")

        print("Using pprint function \n")
        pprint.pprint(json_data)
        print("-----done--------")

        # iterates through the dictionary and prints key value pairs
        for key, value in json_data[0].items():
            print(key, ": ", value)

    except requests.exceptions.RequestException as e:
        print("Error:", {e})


random_brew()
