from dispatcher import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text
from bd import *
from keyboard import *
new_user = """
<em>Вітаємо <b>{name}</b> у боті для знайомств NTUDP.
Для початку спілкування заповніть, будь ласка, свій профіль.
</em>
"""
return_user = """
<em>З поверненням <b>{name}</b> рад вас знову бачити❤️</em>
"""
profil_text = """
Профіль
	Ім'я:{name}
	Група:{group}
	Вік:{age}
"""
filter_text = """
Фільтр
	Спеціальність:{group}
	Вік:{age}
"""


def reg_check(id):
    adminList = get_user_info(None, "id")
    check_id = False
    for item in adminList:
        if item[0] == id:
            check_id = True
            break
    return check_id


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if reg_check(message.chat.id):
        username = get_profil_info(get_user_info(
            message.chat.id, "code"), 'name')
        if username == 'none':
            username = message.from_user.first_name
        await message.answer(return_user.format(name=username), parse_mode="HTML", reply_markup=start_menu)
    else:
        await message.answer(new_user.format(name=message.from_user.first_name), parse_mode="HTML", reply_markup=start_menu)
        await create_user(message.chat.id)
    await change_user_info(message.chat.id, 'mess_id', 0)
    await message.delete()


@dp.message_handler(Text("Профіль"))
async def profil(message: types.Message):
    profilInfo = get_profil_info(get_user_info(message.chat.id, "code"), '*')
    mess_id = get_user_info(message.chat.id, "mess_id")
    if mess_id == 0:
        mess = await message.answer(profil_text.format(
            name='Не вказано' if profilInfo[1] == 'none' else profilInfo[1],
            group='Не вказано' if profilInfo[2] == 'none' else profilInfo[2],
            age='Не вказано' if profilInfo[3] == 0 else profilInfo[3]),
            reply_markup=change_user_info_button)
        await change_user_info(message.chat.id, 'mess_id', mess.message_id)
    else:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=mess_id,
                                    text=profil_text.format(
                                        name='Не вказано' if profilInfo[1] == 'none' else profilInfo[1],
                                        group='Не вказано' if profilInfo[2] == 'none' else profilInfo[2],
                                        age='Не вказано' if profilInfo[3] == 0 else profilInfo[3]),
                                    reply_markup=change_user_info_button)
    await change_user_info(message.chat.id, 'type_activ', 'none')
    if message.text == 'Профіль':
        await message.delete()


@dp.message_handler(Text("Фільтр"))
async def search_filters(message: types.Message):
    filterInfo = get_filter_info(get_user_info(message.chat.id, "code"), '*')
    mess_id = get_user_info(message.chat.id, "mess_id")
    if mess_id == 0:
        mess = await message.answer(
            filter_text.format(
                group='Не вказано' if filterInfo[1] == 'none' else filterInfo[1],
                age='Не вказано' if filterInfo[2] == 'none' else filterInfo[2]),
            reply_markup=change_filter_info_button)
        await change_user_info(message.chat.id, 'mess_id', mess.message_id)
    else:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=mess_id,
                                    text=filter_text.format(
                                        group='Не вказано' if filterInfo[1] == 'none' else filterInfo[1],
                                        age='Не вказано' if filterInfo[2] == 'none' else filterInfo[2]),
                                    reply_markup=change_filter_info_button)
    await change_user_info(message.chat.id, 'type_activ', 'none')
    await message.delete()


@dp.message_handler(content_types=types.ContentType.TEXT)
async def typing(message: types.Message):
    type_activ = get_user_info(message.chat.id, 'type_activ')
    code = get_user_info(message.chat.id, 'code')
    if type_activ == 'changeN' or type_activ == 'changeG' or type_activ == 'changeA':
        await message.delete()
        await change_profil_info(code, 'name' if type_activ == 'changeN'else
                                       'grupa' if type_activ == 'changeG'else
                                       'age', message.text)
        await profil(message)
    elif type_activ == 'changeFG' or type_activ == 'changeFA':
        await message.delete()
        await change_filter_info(code, 'grupa' if type_activ == 'changeFG'else
                                       'age', message.text)
        await search_filters(message)
