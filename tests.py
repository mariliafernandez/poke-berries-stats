import pytest
from requests import RequestException
from load_data import get_all_berry_results, get_data_from_results
import stats
import numpy as np


class TestStats:
    array = [1,1,2,2,2,3,5,5,5,5,5]

    
    def test_get_stats_types(self):

        all_stats = stats.get_stats(self.array)

        assert type(all_stats['min_growth_time']) == int
        assert type(all_stats['median_growth_time']) == float
        assert type(all_stats['max_growth_time']) == int
        assert type(all_stats['variance_growth_time']) == float
        assert type(all_stats['mean_growth_time']) == float
        assert type(all_stats['frequency_growth_time']) == dict 


    def test_get_stats_keys(self):

        all_stats = stats.get_stats(self.array)

        assert "min_growth_time" in all_stats
        assert "median_growth_time" in all_stats
        assert "max_growth_time" in all_stats
        assert "variance_growth_time" in all_stats
        assert "mean_growth_time" in all_stats
        assert "frequency_growth_time" in all_stats


    def test_get_stats_results(self):

        all_stats = stats.get_stats(self.array)

        assert all_stats['min_growth_time'] == np.min(self.array)
        assert all_stats['median_growth_time'] == np.median(self.array)
        assert all_stats['max_growth_time'] == np.max(self.array)
        assert all_stats['variance_growth_time'] == np.var(self.array)
        assert all_stats['mean_growth_time'] == np.mean(self.array)
        assert all_stats['frequency_growth_time'] == {1:2, 2:3, 3:1, 5:5}


class TestLoadData:

    def test_get_all_berry_results(self):
        
        results = get_all_berry_results()

        assert len(results) > 0
        assert type(results) == list

        for result in results:
            assert 'url' in result
            assert 'name' in result


    def test_get_data_from_results(self):

        assert get_data_from_results([]) == {"names":[], "growth_times":[]}
        assert get_data_from_results([{}]) == {"names":[], "growth_times":[]}
        
        result_mock = {'url':'', 'name':''}
        
        with pytest.raises(RequestException):
            get_data_from_results([result_mock])