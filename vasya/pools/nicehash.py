from typing import Union, Dict

import requests

from vasya.pools.abc import PoolInterfaceAbstract


class NicehashPool(PoolInterfaceAbstract):
    command = 'Nicehash'

    def __init__(self, api_id, api_key):
        self.api_id = api_id
        self.api_key = api_key

    def getBalance(self) -> Union[None, Dict[str, str]]:
        resp = requests.get("https://api.nicehash.com/api?method=balance&id=%s&key=%s" % (
            self.api_id, self.api_key,
        ))

        resp_json = resp.json()

        if 'error' in resp_json['result']:
            return {
                "Error": resp_json['result']['error']
            }
        else:
            return {
                "Confirmed": "%s BTC" % resp_json['result']['balance_confirmed'],
                "Pending": "%s BTC" % resp_json['result']['balance_pending'],
            }
