import json
import requests


url = "https://api.openbrewerydb.org/v1/breweries?by_city=miami&per_page=5"
url_random = "https://api.openbrewerydb.org/v1/breweries/random"


def search_brew(url):

    response = requests.get(url)
    print("\nhttp status code: ", response.status_code, "- ", response.reason)
    response.raise_for_status()

    json_data = json.loads(response.text)

    print('\nLoading watering holes...')
    for brewery in json_data:
        for key, value in brewery.items():
            if brewery[key] is not None:
                print(key, ": ", value)
        print("\n")


def main_menu():  # Displays the main menu options
    print("Welcome to BrewFinder - please select an option.\n")
    print("1. Pick a random brewery")
    print("2. Search by US city")
    print("3. Search by brewery type")
    print("4. Find your nearest brewery")
    print("5. Exit BrewFinder")


def main_menu_option(option):  # Handles main menu option selections
    if option == 1:
        print("Picking a random brewery somewhere, someplace...")
        search_brew(url_random)
    if option == 2:
        by_city = input("Pick a US city:")
        search_brew("https://api.openbrewerydb.org/v1/breweries?by_city=" + by_city)
    elif option == 5:
        print("Thanks for using BrewFinder. Safe journey home")
        exit()
    else:
        print("Invalid option. Please try again\n")


while True:  # Runs main_menu() unless option 4 is selected (This calls exit())
    main_menu()
    try:
        option = int(input("Enter your choice: "))
        main_menu_option(option)
    except ValueError:  # catches non number but needs to be between 1 and 4
        print("Invalid: Option needs to be a number between 1 and 4")
