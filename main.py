from aiogram import executor
from aiogram.dispatcher.filters import Text
import logging

from config import dp
from handlers.echo import picture, myinfo
from handlers.start import (
    start,
    cmd_help,
)
from handlers.user_info_fsm import (
    UserForm,
    start_user_dialog,
    process_age,
    process_name,
    process_address,
    process_day,
    mail,
    not_mail
)

if __name__ == "__main__":
    print(__name__)
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(start_user_dialog, commands=["form"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_address, state=UserForm.address)
    dp.register_message_handler(process_day, state=UserForm.day)
    dp.register_callback_query_handler(mail, Text(startswith="да"))
    dp.register_callback_query_handler(not_mail, Text(startswith="нет"))
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_message_handler(myinfo, commands=["myinfo"])

    executor.start_polling(dp, skip_updates=True)
