import requests


def get_all_berry_results():

    next_page = 'https://pokeapi.co/api/v2/berry/?offset=20&limit=20'
    results = []

    while next_page:

        print(next_page)
        
        response = requests.get(next_page).json()
        next_page = response['next']
        results += response['results']

    return results
