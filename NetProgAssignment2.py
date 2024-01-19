import json  # imports json library
import requests  # imports requests library


def get_url(url):  # Receives url as an argument from search_brew() and get_distance()
    try:
        response = requests.get(url)  # uses http GET to fetch data from the API
        print("\nhttps status code: {0} - {1}".format(response.status_code, response.reason))
        json_data = json.loads(response.text)  # parses response into a Python dictionary

    except requests.exceptions.RequestException as error:  # Catches http errors if they occur
        if error is not None:
            print("https error: {0}" .format(error))
            exit()
    return json_data  # returns json data to the function that has called get_url()


def search_brew(url):
    base_url = "https://api.openbrewerydb.org/v1/breweries"  # Consistent url for the API

    json_data = get_url(base_url+url)  # Calls get_url, passes base_url and params as a single string

    print("\nLoading watering holes...")
    for brewery in json_data:  # Iterates through list of breweries, then through each one's key-value pair
        for key, value in brewery.items():
            if brewery[key] is not None and brewery[key] is not brewery['id']:  # ignores blank and 'id' key- value pair
                print(key, ": ", value)  # Prints key-value pairs in a nice format
        print("\n")
    print("-----End of results-----\n")


def get_nearest():  # Finds lattitude and longitude based on a city name and 2-letter country code
    city = input("Choose a city: ")
    c_code = input("Choose a 2 letter country code: ")
    api = "SLCojxErejjcKrDlee14xw==HjGimltRFWPEoGjO"  # Api key and url on seperate lines to enhance readability
    url = ("https://api.api-ninjas.com/v1/geocoding?city={0}&country={1}&x-Api-Key={2}&per_page=3"
           .format(city, c_code, api))

    json_data = get_url(url)  # Calls get_url, passes base_url and params as a single string

    for latlong in json_data:  # Iterates through json_data to find key-value pair
        for key, value in latlong.items():
            if latlong[key] is None:
                print("Location not found")
        by_lat = latlong['latitude']
        by_long = latlong['longitude']

        return by_lat, by_long  # Returns lattitude and longitude


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

    elif option == 2:  # Takes by_city & by_type input and concatenates them into a string to pass to search_brew
        by_city = input("Pick a US city, or enter for all: ")
        by_type = input("Pick a brewery type: micro, nano, regional, brewpub, or press enter for all: ").lower()
        if by_type in ['Micro', 'Nano', 'Regional', 'Brewpub']:
            search_brew("?by_city={0}&by_type={1}" .format(by_city, by_type))
        else:
            print("Showing all results for: {0}".format(by_city))
            search_brew("?by_city={0}&per_page=5".format(by_city))

    elif option == 3:
        print("Choose a city and 2 letter country code:\n")
        by_lat, by_long = get_nearest()  # Return values passed to search_brew as arguments / url parameters
        search_brew("?by_dist={0},{1}&per_page=5".format(by_lat, by_long))

    elif option == 4:  # Exits application
        print("\nThanks for using BrewFinder. Safe journey home")
        exit()

    else:  # Ensures user only enters 1 - 4
        print("Invalid: Option must be a number between 1 and 4\n")


while True:  # Continuously calls main_menu() unless option 4 is selected (This calls exit())
    main_menu()
    try:
        option = int(input("\nChoose an option: "))
        main_menu_option(option)
    except ValueError:  # Catches non-numerical entries
        print("Invalid: Option must be a number between 1 and 4\n")
