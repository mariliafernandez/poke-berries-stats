from flask import Flask
import json

app = Flask(__name__)

@app.route("/allBerryStats", methods=['GET'])
def all_berry_stats():

    response = {
        "berries_names": list(),
        "min_growth_time": "",
        "median_growth_time": "",
        "max_growth_time": "",
        "variance_growth_time": "",
        "mean_growth_time": "",
        "frequency_growth_time": ""
    }

    return json.dumps(response)