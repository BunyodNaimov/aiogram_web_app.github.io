
from aiogram import types, Dispatcher

from aiogram.filters import CommandStart

from keyboards import site_kb

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom", reply_markup=site_kb)
