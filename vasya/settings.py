import configparser
import typing

from vasya.pools.abc import PoolInterfaceAbstract
from vasya.pools import POOL_MAPPING

parser = configparser.ConfigParser()
parser.read('settings.ini')

TOKEN: str = parser.get('bot', 'token')
POOLS: typing.Dict[typing.Type[PoolInterfaceAbstract], typing.Dict] = {}

for section in parser.sections():
    if section.startswith("pool-"):
        poolinterface = POOL_MAPPING.get(section[5:], None)  # type: typing.Type[PoolInterfaceAbstract]
        if poolinterface is None:
            raise ValueError("Unknown pool: %s" % section[5:])
        POOLS[poolinterface] = dict(parser.items(section))  # type: ignore
