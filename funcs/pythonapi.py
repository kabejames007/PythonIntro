import requests
import json

base_url = "https://swapi.info/api/"
def get_characters_info():
    url = base_url + "people/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch character information.")
        return None

data = get_characters_info()
print(data[1]['name'])
print(data[1]['height'])    # Print the height of the first character
print(data[1]['mass'])     # Print the mass of the first character


def get_people_info(id: int) -> int:
    url = base_url + "people/" + str(id)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch planet information.")
        return None

people = get_people_info(1)
print(people)