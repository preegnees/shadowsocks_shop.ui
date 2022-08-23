from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from consts.consts import *

get_history = KeyboardButton(HISTORY)
get_status = KeyboardButton(STATUS)
info_about_bot = KeyboardButton(INFO)
get_instructions_vpn = KeyboardButton(INSTRUCTION)

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.row(
    get_status, get_history
).row(
    info_about_bot, get_instructions_vpn
)

pay = KeyboardButton(PAY)
cancel = KeyboardButton(CANCEL)
status_kb = ReplyKeyboardMarkup(resize_keyboard=True)
status_kb.row(
    pay, cancel
)
