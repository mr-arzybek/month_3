from aiogram import types

async def on_user_joined(message: types.Message):
    await message.delete()

async def filter_messages(message: types.Message):
    if "Плохое слово" in message.text:
        await message.delete()

async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('это команда должна быть ответом на сообщение!')
        return
    await message.bot.delete_message(chat_id=config.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID,user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('Пользователь забанен!')