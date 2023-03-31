from aiogram import types
from dispatcher import *
from aiogram.dispatcher.filters import Text
from keyboard import *
from bd import *


@dp.callback_query_handler(Text("changeN") | Text("changeG") | Text("changeA"))
async def change_profil(c: types.CallbackQuery):
    await c.message.edit_text("Введіть Ім'я"if c.data == "changeN" else
                              "Введіть Групу" if c.data == "changeG" else
                              "Введіть Вік")
    await change_user_info(c.message.chat.id, 'type_activ', c.data)


@dp.callback_query_handler(Text("changeFG") | Text("changeFA"))
async def change_filter(c: types.CallbackQuery):
    await c.message.edit_text("Введіть спеціальність у числовому форматі.\nНа приклад Комп'ютерні  науки: 122.\nДля зняття фільтра введіть none" if c.data == "changeFG" else "Введіть діапазон  віку у форматі від-до.\nНа приклад від 18 до 20: 18-20.\nДля зняття фільтра введіть none")
    await change_user_info(c.message.chat.id, 'type_activ', c.data)
