""" """
from pathlib import Path
import json
import os
from datetime import datetime
from typing import Union, List
import pandas as pd
from polygon import RESTClient


# pandas dataframe display settings
pd.set_option("display.max_columns", None)
pd.set_option('display.width', 1000)

# public constants
INTRADAY_INTERVALS = ["second", "minute", "hour"]

# private constants
_DATE_FORMAT = "%Y-%m-%d"
_ALLOWED_TIMESPAN = [*INTRADAY_INTERVALS,
                     "day", "week", "month", "quarter", "year"]


class StockDataClient:
    def __init__(self, api_key):
        self.client = RESTClient(api_key)

    def get_data(
        self,
        symbol: str,
        # ex: "<multiplier> <timespan>", "1 minute"
        intervals: Union[List[str], str],
        start_date: str,  # YYYY-MM-DD
        end_date: str = None  # YYYY-MM-DD
    ):

        # validate intervals
        if isinstance(intervals, str):
            intervals = [intervals]
        _intervals = []
        for interval in intervals:
            interval_split = interval.split(" ")
            try:
                multiplier = int(interval_split[0])
            except Exception as _:
                multiplier = None
            timespan = interval_split[1]

            if timespan not in _ALLOWED_TIMESPAN or not multiplier:
                raise Exception(f"Invalid interval. Must be in format '<multiplier> <timespan>'.\n"
                                f"Multiplier must be an int.\n"
                                f"Allowed timespans: {_ALLOWED_TIMESPAN}\n."
                                f"Ex: '1 minute'.")
            _intervals.append((multiplier, timespan))

        # validate dates
        if not end_date:
            end_date = datetime.now().strftime(_DATE_FORMAT)
        for _type, _date in zip(["start", "end"], [start_date, end_date]):
            try:
                datetime.strptime(_date, _DATE_FORMAT)
            except Exception as _:
                raise Exception(f"Invalid {_type}_date. Must be in format '{_DATE_FORMAT}'.\n"
                                f"Ex: '2023-12-31'.")

        # pull data
        data = {}
        for multiplier, timespan in _intervals:
            timeseries = [_d for _d in self.client.list_aggs(
                ticker=symbol, multiplier=multiplier, timespan=timespan, from_=start_date, to=end_date, limit=50000
            )]
            df = pd.DataFrame(timeseries)
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit="ms")
            data[f"{multiplier} {timespan}"] = df

        return data


if __name__ == "__main__":
    path = Path(__file__).parent / "config.json"

    with open(path, "r") as rd:
        lines = rd.read()
        config = json.loads(lines)

    # print(config)

    client = StockDataClient(api_key=config["polygon_api_key"])
    stock_data = client.get_data(
        symbol="NDAQ",  # to get data of different stocks change symbol to desired ticker
        # can change interval of data 1day, 1hour, 15min, etc.
        intervals=["1 day"],
        start_date="2019-01-01"  # date 5 years back is the max we can go
    )

    for interval, data in stock_data.items():
        print("-"*150)
        print(interval)
        print(data)
        path_to_data_file = Path(__file__).parent / \
            "data" / "nasdaq20190101.csv"
        data.to_csv(path_to_data_file, index=False)
