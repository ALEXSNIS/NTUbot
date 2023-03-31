from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
profil = KeyboardButton("Профіль")
connect = KeyboardButton("Шукати співрозмовника")
filter_to_search = KeyboardButton("Фільтр")
start_menu.add(profil).insert(filter_to_search).add(connect)

change_user_info_button = InlineKeyboardMarkup(row_width=2)
change_name = InlineKeyboardButton("Змінити ім'я", callback_data="changeN")
change_group = InlineKeyboardButton("Змінити групу", callback_data="changeG")
change_age = InlineKeyboardButton("Змінити вік", callback_data="changeA")
change_user_info_button.add(change_name, change_group, change_age)

change_filter_info_button = InlineKeyboardMarkup(row_width=2)
filter_group = InlineKeyboardButton(
    "Задати спеціальність", callback_data="changeFG")
filter_age = InlineKeyboardButton(
    "Задати обмеження віку", callback_data="changeFA")
change_filter_info_button.add(filter_group, filter_age)
