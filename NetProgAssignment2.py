import json
import requests


def get_url(url):
    try:
        response = requests.get(url)
        print("\nhttps status code: {0} - {1}".format(response.status_code, response.reason))
        json_data = json.loads(response.text)

    except requests.exceptions.RequestException as error:
        if error is not None:
            print("https error: {0}" .format(error))
            exit()
    return json_data


#  Main search function. Receives url from
def search_brew(url):
    base_url = "https://api.openbrewerydb.org/v1/breweries"

    json_data = get_url(base_url+url)

    print("\nLoading watering holes...")
    for brewery in json_data:
        for key, value in brewery.items():
            if brewery[key] is not None and brewery[key] is not brewery['id']:  # ignores blank and 'id' key-pair
                print(key, ": ", value)
        print("\n")
    print("-----End of results-----\n")


def get_nearest():
    city = input("Choose a city: ")
    c_code = input("Choose a 2 letter country code: ")
    api = "SLCojxErejjcKrDlee14xw==HjGimltRFWPEoGjO"
    url = "https://api.api-ninjas.com/v1/geocoding?city={0}&country={1}&x-Api-Key={2}&per_page=3".format(city, c_code, api)

    json_data = get_url(url)

    for latlong in json_data:
        for key, value in latlong.items():
            if latlong[key] is None:
                print("Location not found")
        by_lat = latlong['latitude']
        by_long = latlong['longitude']

        return by_lat, by_long


def main_menu():  # Displays the main menu options
    print("Welcome to BrewFinder - please select an option.\n")
    print("1. Pick a random brewery")
    print("2. Search by brewery location and type")
    print("3. Find your nearest brewery")
    print("4. Exit BrewFinder")


def main_menu_option(option):  # Handles main menu option selections

    if option == 1:
        print("Picking a random brewery somewhere, someplace...")
        search_brew("/random")

    elif option == 2:  # This will need some form of exception handling
        by_city = input("Pick a US city, or enter for all: ")  # .lower()  # api only accepts lower case for by_type
        by_type = input("Pick a brewery type: micro, nano, regional, brewpub, or press enter for all: ").lower()
        if by_type in ['Micro', 'Nano', 'Regional', 'Brewpub']:
            search_brew("?by_city={0}&by_type={1}" .format(by_city, by_type))
        else:
            print("Showing all results for: {0}".format(by_city))
            search_brew("?by_city={0}&per_page=5".format(by_city))

    elif option == 3:
        print("Choose a city and 2 letter country code:\n")
        by_lat, by_long = get_nearest()
        search_brew("?by_dist={0},{1}&per_page=5".format(by_lat, by_long))

    elif option == 4:
        print("\nThanks for using BrewFinder. Safe journey home")
        exit()

    else:
        print("Invalid: Option must be a number between 1 and 4\n")


while True:  # Runs main_menu() unless option 5 is selected (This calls exit())
    main_menu()
    try:
        option = int(input("\nChoose an option: "))
        main_menu_option(option)
    except ValueError:  # catches non number but needs to be between 1 and 4
        print("Invalid: Option must be a number between 1 and 4\n")
