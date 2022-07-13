import requests


def get_obj_key(obj, key, default=''):

    if key in obj:
        return obj[key]

    return default


def get_all_berry_results():

    next_page = 'https://pokeapi.co/api/v2/berry/?offset=20&limit=20'
    results = []

    while next_page:

        response = requests.get(next_page).json()
        results += get_obj_key(response, 'results', [])
        next_page = get_obj_key(response, 'next', None)

    return results



def get_data_from_results(result_list):

    names = []
    growth_times = []

    for result in result_list:

        if 'url' in result:
            response = requests.get(result['url']).json()

            growth_time = get_obj_key(response, 'growth_time', -1)
            growth_times.append(growth_time)
            
            name = get_obj_key(result, 'name')
            names.append(name)

    return {"names":names, "growth_times":growth_times}


def get_growth_data():

    all_berry_results = get_all_berry_results()
    return get_data_from_results(all_berry_results)

