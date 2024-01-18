import requests
import json


def get_lat_long():
    city = input("Choose a city: ")
    c_code = input("Choose a 2 letter country code")
    api = "SLCojxErejjcKrDlee14xw==HjGimltRFWPEoGjO"
    url = "https://api.api-ninjas.com/v1/geocoding?city={0}&country={1}&x-Api-Key={2}".format(city, c_code, api)

    # Could I turn the next 5 lines into a function to save space?
    response = requests.get(url)
    print("\nhttp status code: ", response.status_code, "- ", response.reason)
    response.raise_for_status()

    json_data = json.loads(response.text)

    print('\nLets see where you are...')

    for latlong in json_data:
        #for key, value in latlong.items():
            # if latlong[key] is not None:
            #  print(key, ": ", value)
        lat = latlong['latitude']
        long = latlong['longitude']
        by_lat = str(lat)
        by_long = str(long)
    return by_lat, by_long


# by_lat, by_long = get_lat_long()


print(type(by_lat))

print("LAT:", by_lat)
print("LONG", by_long)