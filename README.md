# poke-berries-stats

## Install and run

* Install poetry
    ```
    pip install poetry
    ```

* Clone project
    ```
    git clone https://github.com/mariliafernandez/trading-python-api.git
    ```

* Go to project dir
    ```
    cd trading-python-api
    ```

* Install project dependencies
    ```
    poetry install
    ```

* Activate virtual environment
    ```
    poetry shell
    ```

* Run server
    ```
    [venv] flask run
    ```

## Endpoint

### /allBerryStats [GET]

* **Response**

    ```json
    {
        "berries_names": [...],
        "min_growth_time": "int",
        "median_growth_time": "float",
        "max_growth_time": "int",
        "variance_growth_time": "float",
        "mean_growth_time": "float",
        "frequency_growth_time": {"growth_time (int)": "frequency (int)", ...}
    }
    ```