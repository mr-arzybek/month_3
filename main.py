from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.full_name}"
    )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        f"""

        /start - приветствует по имени
        /help - показывает список команд
        /myinfo - отправляет пользователю его данные(id, first_name, username)
        /picture - отправляет слуайную картинку

        """
    )


@dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    await message.answer(
        f"ID         {message.from_user.id}\n"
        f"FIRST_NAME {message.from_user.first_name}\n"
        f"USER_NAME  {message.from_user.username}\n"
    )


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    img = ["img/img_1.png", "img/img_2.png", "img/img_3.png"]
    photo = open(random.choice(img), "rb")
    await message.answer_photo(
        photo
    )


@dp.message_handler()
async def all(message: types.Message):
    c = len(message.text)
    if c > 3:
        await message.answer(
            message.text.upper()
        )
    else:
        await message.answer(
            message.text
        )


executor.start_polling(dp)




