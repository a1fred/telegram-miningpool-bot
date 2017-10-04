import typing
from telebot import TeleBot, types

from vasya.pools.abc import PoolInterfaceAbstract


def get_bot(token: str, pools: typing.Dict[str, PoolInterfaceAbstract]) -> TeleBot:
    bot = TeleBot(token)

    def end_msg(message):
        markup = types.ReplyKeyboardMarkup()
        [markup.row(p) for p in pools]
        bot.send_message(
            message.chat.id, 
            "Choose pool:", 
            reply_markup=markup
        )

    @bot.message_handler(content_types=["text"])
    def repeat_all_messages(message):
        pool = pools.get(message.text.lower())

        if pool:
            bals = pool.getBalance()
            if bals:
                bot.send_message(
                    message.chat.id, 
                    text="\n".join(["%s: *%s*" % (c, u) for c, u in bals.items()]),
                    reply_to_message_id=message.message_id, parse_mode='Markdown'
                )
        else:
            pass
            end_msg(message)

    return bot
