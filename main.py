import typing

from vasya import settings
from vasya.pools.abc import PoolInterfaceAbstract

pools: typing.Dict[str, PoolInterfaceAbstract] = {}
for p, kwargs in settings.POOLS.items():
    pools[p.command.lower()] = p(**kwargs)


if __name__ == '__main__':
    from vasya import get_bot
    bot = get_bot(settings.TOKEN, pools)

    bot.polling(none_stop=True)
