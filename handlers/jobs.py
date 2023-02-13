from aiogram import types
from config import bot


kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Курьером")
)
kb.add(
    types.KeyboardButton("Сборщиком")
)
kb.add(
    types.KeyboardButton("товароведом")
)

# async def show_jobs(message: types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(
#         chat_id=chat_id,
#         text="Доброго времени суток кем вы хотите работать ? ",
#         reply_markup=kb
#     )

async def show_jobs(call: types.CallbackQuery):
    await call.message.answer(
        text="Мы можем вам подобрать работу",
        reply_markup=kb
    )

async def show_courier(message: types.Message):
    await message.reply("""
    🚚 В логистическую компанию 🛻
                                                        
        🚙  ОЗОН 🛻 
Требуется ‼️
          
🚙Авто КУРЬЕРЫ СО СВОИМ ВЕЛОСИПЕДОМ🚙

🔥Самые лучшие условия работы на рыке 🔥

♨️график выбираете сами 5\2 6\1 7\0 2\2 1\2 3\3♨️
                                      
💵 ЗА ЗАКАЗ 156р💵
💰В день от 4500 и выше 💰
Выплаты каждую неделю 

⏰смена длиться 12 ч 
                                              
☎️ ТЕЛЕФОН : +79651354855
🏢 Адрес офиса: 
👉 м. Бауманская. Ул. Малая Почтовая, дом 12, кабинет 308
⏰Режим приема: 
👉Пн-Пт с 10:00 до 18:00, Субботу с 10:00 до 15:00👈
    """)

async def show_collector(message: types.Message):
    await message.reply("""
    Доброго времени суток !! 😇
Здесь вы найдете горящие вакансии по Москве у вашего дома 🏬!!
Такие как :
АВТО - ВВЕЛО Курьер 🚲🚗
Сборщик заказов 👩🏻‍🌾🧑🏻‍🌾
Пекари 👩🏻‍🍳👨🏻‍🍳
Уборщики🧑🏻‍💼
Грузчики👷🏻

Лучшие условия труда ‼️
выплаты без задержек 💸
Отличный коллектив ♨️
    """)

async def show_merchandiser(message: types.Message):
    await message.reply("""
    СРОЧНО‼️ СРОЧНО ‼️
🚲 В логистическую компанию 🛴
                                                        
         🚲 ОЗОН  🚲
Требуется ‼️
          
🚲ВЕЛО КУРЬЕР СО СВОИМ ВЕЛОСИПЕДОМ🚲

🔥Самые лучшие условия работы на рыке 🔥

♨️график выбираете сами 5\2 6\1 7\0 2\2 1\2 3\3♨️
                                      
💵 ЗА ЗАКАЗ 139р💵
💰В день от 3500 и выше 💰
Выплаты каждую неделю 

⏰смена длиться 12 ч 
                                              
☎️ ТЕЛЕФОН : +79651354855
🏢 Адрес офиса: 
👉 м. Бауманская. Ул. Малая Почтовая, дом 12, кабинет 308
⏰Режим приема: 
👉Пн-Пт с 10:00 до 18:00, Субботу с 10:00 до 15:00👈
    """)
