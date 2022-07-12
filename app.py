import json
from flask import Flask
from load_data import get_growth_data
from stats import get_stats

app = Flask(__name__)

@app.route("/allBerryStats", methods=['GET'])
def all_berry_stats():

    try:
        growth_data = get_growth_data()
    except Exception as e:
        response = {"Error": str(e)}
        return (response, 500, {"content-type":"application/json"})
        

    growth_times = growth_data['growth_times']
    names = growth_data['names']

    response = {"berries_names": names}
    response.update(get_stats(growth_times))

    return (response, {"content-type":"application/json"})