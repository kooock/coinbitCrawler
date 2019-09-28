import requests
import json
import http
from decimal import Decimal
from collections import OrderedDict
from pprint import pprint


def get_trade_pair_data(url):
    res = requests.get(url)
    if res.status_code == http.HTTPStatus.OK:
        return json.loads(res.text)
    return None

def get_acc_value24_pair(data,exchange):
    volumes = []
    for pair in data:
        if pair["division"] == exchange:
            volumes.append((pair["base_korean_name"], Decimal(pair["acc_trade_value_24h"])))
    volumes.sort(key = lambda element : element[1],reverse=True)
    volume_pair = OrderedDict(volumes)
    return volume_pair

def run_crawler():
    data = get_trade_pair_data("https://production-api.coinbit.global/api/v1.0/trading_pairs/")
    volume_pair = get_acc_value24_pair(data,"TWO")
    pprint(volume_pair)

    sum_volumes = sum(volume_pair.values())

    print("sum : {}".format(sum_volumes))

if __name__ == "__main__":
    run_crawler()