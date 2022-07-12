import requests


def get_all_berry_results():

    next_page = 'https://pokeapi.co/api/v2/berry/?offset=20&limit=20'
    results = []

    while next_page:

        response = requests.get(next_page).json()
        results += response['results']
        next_page = response['next']

    return results



def get_data_from_results(result_list):

    names = []
    growth_times = []

    for result in result_list:

        response = requests.get(result['url']).json()

        names.append(result['name'])
        growth_times.append(response['growth_time'])

    return {"names":names, "growth_times":growth_times}


def get_growth_data():

    all_berry_results = get_all_berry_results()
    return get_data_from_results(all_berry_results)

