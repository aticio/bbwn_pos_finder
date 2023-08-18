#!/usr/bin/env python
import sys
import os
import json

from bbwn_pos_finder.repository.memrepo import MemRepo
from bbwn_pos_finder.repository.binance.binancerepo import BinanceRepo
from bbwn_pos_finder.repository.yahoo.yahoorepo import YahooRepo
from bbwn_pos_finder.repository.yahoo.yahoorepo_tr import YahooRepoTR
from bbwn_pos_finder.repository.yahoo.yahoorepo_fx import YahooRepoFX
from bbwn_pos_finder.use_cases.analyze import analyze
from bbwn_pos_finder.use_cases.list_pairs import list_pairs
from bbwn_pos_finder.requests.analyze import build_analyze_request


APPLICATION_CONFIG_PATH = "config"


def analyze_single(symbol, repo_type, interval):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    request = build_analyze_request({"symbol": symbol, "interval": interval, "bbwn_length": 20, "bbwn_std": 2, "ssf_length_1": 15, "ssf_length_2": 30})

    result = analyze(repo, request)
    print(result.value)


def analyze_all(repo_type, interval):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    response = list_pairs(repo)
    list_of_results = []
    for symbol in response.value:
        request = build_analyze_request({"symbol": symbol, "interval": interval, "bbwn_length": 20, "bbwn_std": 2, "ssf_length_1": 15, "ssf_length_2": 30})

        response = analyze(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.open_position is True:
                list_of_results.append(result_object)

    for res in list_of_results:
        print(res.symbol)


def setenv(variable, default):
    os.environ.setdefault(variable, default)


def app_config_file(config):
    return os.path.join(APPLICATION_CONFIG_PATH, f"{config}.json")


def read_json_configuration(config):
    # Read configuration from the relative JSON file
    with open(app_config_file(config)) as f:
        config_data = json.load(f)

    # Convert the config into a usable Python dictionary
    config_data = dict((i["name"], i["value"]) for i in config_data)

    return config_data


def configure_app(config):
    configuration = read_json_configuration(config)

    for key, value in configuration.items():
        setenv(key, value)


if __name__ == "__main__":
    config = sys.argv[1]
    configure_app(config)
    if sys.argv[2] == "analyze_single":
        symbol = sys.argv[3]
        repo_type = sys.argv[4]
        interval = sys.argv[5]
        analyze_single(symbol, repo_type, interval)
    elif sys.argv[2] == "analyze_all":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        analyze_all(repo_type, interval)
