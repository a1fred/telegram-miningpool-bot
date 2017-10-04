from typing import Union, Dict

import requests

from vasya.pools.abc import PoolInterfaceAbstract


class BitcoinComPool(PoolInterfaceAbstract):
    command = 'Bitcoin.com'

    def __init__(self, api_key):
        self.api_key = api_key

    def getBalance(self) -> Union[None, Dict[str, str]]:
        resp = requests.get("https://console.pool.bitcoin.com/srv/api/user?apikey=%s" % (
            self.api_key,
        ))

        resp_json = resp.json()
        return {
            "BTC balance": "%s BTC" % str(resp_json['bitcoinBalance']), 
            "BCC balance": "%s BCC" % str(resp_json['bitcoinCashBalance']),
        }
