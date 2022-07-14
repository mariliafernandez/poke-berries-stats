import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_frequency(array):

    frequency_values = dict()
    
    values, frequency = np.unique(array, return_counts=True)

    for val, freq in zip(values, frequency):
        frequency_values[int(val)] = int(freq)

    return frequency_values


def get_min(array):
    return int(np.min(array))


def get_max(array):
    return int(np.max(array))


def get_variance(array):
    return float(np.var(array))


def get_median(array):
    return float(np.median(array))


def get_mean(array):
    return float(np.mean(array))


def generate_histogram_b64(data):

    growth_time = list(data.keys())
    frequency = list(data.values())

    min = get_min(growth_time)
    max = get_max(growth_time)

    plt.title('Histogram')
    plt.xlabel('Growth Time (hours)')
    plt.ylabel('Frequency')
    plt.hist(growth_time, weights=frequency)
    plt.xticks([i for i in range(min, max+1, 2)])

    tmp = BytesIO()
    plt.savefig(tmp, format='png')

    encoded = base64.b64encode(tmp.getvalue()).decode('utf-8')   

    return encoded    


def generate_histogram_html(data, template_name):

    img_b64 = generate_histogram_b64(data)
    html = f"<html><body><img src=\'data: image/png;base64, {img_b64}\'/></body></html>"

    with open(f'templates/{template_name}.html', 'w') as f:
        f.write(html)


def get_stats(data:list):

    np_data = np.asarray(data)

    return {
        "min_growth_time": get_min(np_data),
        "median_growth_time": get_median(np_data),
        "max_growth_time": get_max(np_data),
        "variance_growth_time": get_variance(np_data),
        "mean_growth_time": get_mean(np_data),
        "frequency_growth_time": get_frequency(np_data),
    }


