from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from bot.markup import start_kb, status_kb
from consts.consts import *

from from_server.response import Responser

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("token")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

resp = Responser()


@dp.message_handler(commands=[START])
async def start_command(message: types.Message):
    await message.reply(resp.start_to_message(), reply_markup=start_kb)


@dp.message_handler(commands=[HELP])
async def help_command(message: types.Message):
    await message.reply(resp.help_to_message())


@dp.message_handler(lambda message: message.text == HISTORY)
async def history_command(message: types.Message):
    await message.reply(resp.history_to_message())


@dp.message_handler(lambda message: message.text == INFO)
async def info_command(message: types.Message):
    await message.reply(resp.info_to_message())


@dp.message_handler(lambda message: message.text == INSTRUCTION)
async def instruction_command(message: types.Message):
    await message.reply(resp.instruction_to_message())


@dp.message_handler(lambda message: message.text == CANCEL)
async def cancel_command(message: types.Message):
    await message.reply(resp.cansel_to_message(), reply_markup=start_kb)


@dp.message_handler(lambda message: message.text == PAY)
async def paid_command(message: types.Message):
    await message.reply(resp.paid_to_message(), reply_markup=start_kb)


@dp.message_handler(lambda message: message.text == STATUS)
async def status_command(message: types.Message):
    (status, ok) = resp.status_to_message()
    if ok:
        await message.reply(status, reply_markup=start_kb)
    else:
        await message.reply(status, reply_markup=status_kb)


@dp.message_handler()
async def other_command(message: types.Message):
    await message.reply(resp.other_to_message())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
