"""
Set of modules to access to some mining pools stats
"""

import typing
from vasya.pools import abc
from vasya.pools import bitcoin_com, nicehash

POOL_MAPPING: typing.Dict[str, typing.Type[abc.PoolInterfaceAbstract]] = {
    'nicehash': nicehash.NicehashPool,
    'bitcoincom': bitcoin_com.BitcoinComPool,
}
