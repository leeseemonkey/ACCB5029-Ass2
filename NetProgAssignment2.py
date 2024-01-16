import json
import requests


def random_brew():  # Displays a random brewery

    try:

        # simple request to fetch and display data from an api #
        url = "https://api.openbrewerydb.org/v1/breweries?by_city=miami&per_page=3"
        response = requests.get(url)
        print("http status code: ",  response.status_code, "- ", response.reason)
        # response.raise_for_status()

        # json_data = response.json()
        # parses JSON string and converts into a Python dictionary
        # but looks like json is an array so parses it into a list :(
        json_data = json.loads(response.text)
        print(json_data)
        print("Type: ", type(json_data), "\n")
       #  print("The name should be here: ", json_data['name'])
       #  print("City: ", json_data['city'])

        print("JSON array as Python list: ", json_data[0])

        print("Trying iter: ", iter(json_data))

        # json_dict = {}
        # for element in json_data:
        #    json_dict[element] = element
        # print("Dict converter: ", json_dict, "\n")


        # json_data = response.json() # Returns a JSON object of the result (if the result was written in JSON format
        # json_dict = json_data[0]
        # print(json_dict)

        for index, item in enumerate(json_data):
            print("New for loop: ", item)
        print(json_data['name'])

        # iterates through the dictionary and prints key value pairs
        # though this one doesn't iterate, it just looks at the first item.

        # for key, value in enumerate(json_data.items()):
        #    print(key, ": ", value, "\n---------------")

        # for key, value in json_data.items():
        #    print("{} : {} ".format(key, value))

    # is there a better way of printing this error?
    except requests.exceptions.RequestException as e:
        print("Error:", {e})
        print(type(e))


random_brew()
