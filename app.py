from flask import Flask, render_template, request
from jinja2 import TemplateNotFound
from load_data import get_growth_data
from stats import generate_histogram_html, get_stats


app = Flask(__name__)

@app.route("/allBerryStats", methods=['GET'])
def all_berry_stats():

    response = dict()

    try:
        growth_data = get_growth_data()
    except Exception as e:
        response = {'Error': str(e)}
        return (response, 500, {'content-type':'application/json'})
        
    growth_times = growth_data['growth_times']
    names = growth_data['names']
    
    response['berries_names'] = names
    
    stats = get_stats(growth_times)
    response.update(stats)

    template_name = 'histogram'
    generate_histogram_html(stats['frequency_growth_time'], template_name)

    response['histogram_url'] = request.url.replace('allBerryStats', f'histogram/{template_name}')

    return (response, {'content-type':'application/json'})


@app.route('/histogram/<template_name>', methods=['GET'])
def histogram(template_name):

    try:
        return render_template(f'{template_name}.html')
    except TemplateNotFound:
        return ({'Error':'Template not found'}, 404, {'content-type':'application/json'})