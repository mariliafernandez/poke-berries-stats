import numpy as np

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


def get_stats(data:list):

    np_data = np.asarray(data)

    return {
        "min_growth_time": get_min(np_data),
        "median_growth_time": get_median(np_data),
        "max_growth_time": get_max(np_data),
        "variance_growth_time": get_variance(np_data),
        "mean_growth_time": get_mean(np_data),
        "frequency_growth_time": get_frequency(np_data)
    }
