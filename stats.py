import numpy as np

def frequency(data:np.array):

    frequency_values = dict()
    
    values, frequency = np.unique(data, return_counts=True)

    for val, freq in zip(values, frequency):
        frequency_values[int(val)] = int(freq)

    return frequency_values


def get_stats(data:list):

    np_data = np.asarray(data)

    return {
        "min_growth_time": int(np.min(np_data)),
        "median_growth_time": float(np.median(np_data)),
        "max_growth_time": int(np.max(np_data)),
        "variance_growth_time": float(np.var(np_data)),
        "mean_growth_time": float(np.mean(np_data)),
        "frequency_growth_time": frequency(np_data)
    }
