import sqlite3 as sq
import random

global db, cur
db = sq.connect('./bot.db')
cur = db.cursor()


def create_code():
    codes = get_user_info(None, 'code')
    code = ""
    for x in range(6):
        code += random.choice(
            list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    for item in codes:
        if item == code:
            create_code()
    return code


async def create_user(user_id):
    code = create_code()
    cur.execute(f"INSERT INTO user_info VALUES({user_id},'{code}',0,'none')")
    cur.execute(f"INSERT INTO profil_info VALUES('{code}','none','none',0)")
    cur.execute(f"INSERT INTO search_filters VALUES('{code}','none','none')")
    db.commit()

# User Info bd


def get_user_info(user_id, name_info):
    if user_id != None:
        if name_info == "*":
            return cur.execute(f"SELECT {name_info} FROM user_info WHERE id={user_id}").fetchone()
        else:
            return cur.execute(f"SELECT {name_info} FROM user_info WHERE id={user_id}").fetchone()[0]
    else:
        return cur.execute(f"SELECT {name_info} FROM user_info").fetchall()


async def change_user_info(user_id, name_info, value):
    if type(value) == str:
        cur.execute(
            f"UPDATE user_info SET {name_info} = '{value}' WHERE id = {user_id}")
    else:
        cur.execute(
            f"UPDATE user_info SET {name_info} = {value} WHERE id = {user_id}")
    db.commit()

# Profile Info bd


def get_profil_info(code, name_info):
    if code != None:
        if name_info == "*":
            return cur.execute(f"SELECT {name_info} FROM profil_info WHERE code='{code}'").fetchone()
        else:
            return cur.execute(f"SELECT {name_info} FROM profil_info WHERE code='{code}'").fetchone()[0]
    else:
        return cur.execute(f"SELECT {name_info} FROM profil_info").fetchall()


async def change_profil_info(code, name_info, value):
    if type(value) == str:
        cur.execute(
            f"UPDATE profil_info SET {name_info} = '{value}' WHERE code = '{code}'")
    else:
        cur.execute(
            f"UPDATE profil_info SET {name_info} = {value} WHERE code = '{code}'")
    db.commit()

# Filter bd


def get_filter_info(code, name_info):
    if code != None:
        if name_info == "*":
            return cur.execute(f"SELECT {name_info} FROM search_filters WHERE code='{code}'").fetchone()
        else:
            return cur.execute(f"SELECT {name_info} FROM search_filters WHERE code='{code}'").fetchone()[0]
    else:
        return cur.execute(f"SELECT {name_info} FROM search_filters").fetchall()


async def change_filter_info(code, name_info, value):
    if type(value) == str:
        cur.execute(
            f"UPDATE search_filters SET {name_info} = '{value}' WHERE code = '{code}'")
    else:
        cur.execute(
            f"UPDATE search_filters SET {name_info} = {value} WHERE code = '{code}'")
    db.commit()
