import json
import requests
#  import NetProgAssLib


# url = "https://api.openbrewerydb.org/v1/breweries?by_city=miami&per_page=5"


def get_url(url):
    response = requests.get(url)
    print("\nhttp status code: ", response.status_code, "- ", response.reason)
    response.raise_for_status()

    json_data = json.loads(response.text)
    return json_data


def search_brew(url):
    base_url = "https://api.openbrewerydb.org/v1/breweries"
    json_data = get_url(base_url+url)
    print('\nLoading watering holes...')
    for brewery in json_data:
        for key, value in brewery.items():
            if brewery[key] is not None:
                print(key, ": ", value)
        print("\n")
    print("-----End of results-----\n")


def get_lat_long():
    city = input("Choose a city: ")
    c_code = input("Choose a 2 letter country code")
    api = "SLCojxErejjcKrDlee14xw==HjGimltRFWPEoGjO"
    url = "https://api.api-ninjas.com/v1/geocoding?city={0}&country={1}&x-Api-Key={2}&per_page=3".format(city, c_code, api)

    json_data = get_url(url)

    for latlong in json_data:
        #for key, value in latlong.items():
            # if latlong[key] is not None:
            #  print(key, ": ", value)
        lat = latlong['latitude']
        long = latlong['longitude']
        by_lat = str(lat)
        by_long = str(long)
    #  print("\nThe closest breweries to {0}, {1} at lattitude {2} and longitude {3} are: ".format(city, c_code, by_lat,
    #                                                                                            by_long))
        return by_lat, by_long



def main_menu():  # Displays the main menu options
    print("Welcome to BrewFinder - please select an option.\n")
    print("1. Pick a random brewery")
    print("2. Search by brewery type")
    print("3. Find your nearest brewery")
    print("4. Exit BrewFinder")


def main_menu_option(option):  # Handles main menu option selections
    if option == 1:
        print("Picking a random brewery somewhere, someplace...")
        search_brew("/random")

    elif option == 2:  # This will need some form of exception handling
        by_city = input("Pick a US city: ")
        by_type = input("Pick a brewery type: Micro, Nano, Regional, Brewpub, or All: ")
        if by_type in ['Micro', 'Nano', 'Regional', 'Brewpub']:
            search_brew("?by_city={0}&by_type={1}" .format(by_city, by_type.lower()))
        else:  # Had to add the lower method as the API seems to be case-sensitive
            print("Brewery type invalid or not found. Showing all results for: {0}".format(by_city))
            search_brew("?by_city={0}&per_page=5".format(by_city))

    elif option == 3:
        print("Choose a city and 2 letter country code - list of country codes can be found *here*")
        by_lat, by_long = get_lat_long()
        search_brew("?by_dist={0},{1}".format(by_lat, by_long))

    elif option == 4:
        print("\nThanks for using BrewFinder. Safe journey home")
        exit()
    else:
       print("Invalid option. Please try again\n")


while True:  # Runs main_menu() unless option 5 is selected (This calls exit())
    main_menu()
    try:
        option = int(input("\nChoose an option: "))
        main_menu_option(option)
    except ValueError:  # catches non number but needs to be between 1 and 4
        print("Invalid: Option needs to be a number between 1 and 4")
