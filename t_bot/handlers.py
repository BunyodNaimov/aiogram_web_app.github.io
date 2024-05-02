
from aiogram import types, Dispatcher

from aiogram.filters import CommandStart, Command

from keyboards import site_kb
from t_bot.db import db_get_all_products

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom", reply_markup=site_kb)


@dp.message(Command(commands='products'))
async def cmd_products(message: types.Message):
    products = await db_get_all_products()
    for product in products:
        print(product)
        await message.answer(text=f"Product {product[1]}\n"
                                  f"Prise {product[3]}")