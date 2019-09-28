import requests
import json
import http
from decimal import Decimal



def get_trade_pair_data(url):
    res = requests.get(url)
    if res.status_code == http.HTTPStatus.OK:
        return json.loads(res.text)
    return None

def get_acc_volume24_list(data,exchange):
    volumes = []
    for pair in data:
        if pair["division"] == exchange:
            volumes.append(Decimal(pair["acc_trade_volume_24h"]))
    return volumes

def run_crawler():
    data = get_trade_pair_data("https://production-api.coinbit.global/api/v1.0/trading_pairs/")
    volumes = get_acc_volume24_list(data,"TWO")
    print(volumes)

    sum_volumes = sum(volumes)

    print("sum : {}".format(sum_volumes))

if __name__ == "__main__":
    run_crawler()