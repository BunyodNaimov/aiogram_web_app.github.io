from aiogram import types, Dispatcher

from aiogram.filters import CommandStart, Command

from keyboards import site_kb
from t_bot.db import db_get_all_products

dp = Dispatcher()
PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=100000)],
    '2': [types.LabeledPrice(label='Item2', amount=200000)],
    '3': [types.LabeledPrice(label='Item3', amount=300000)],
    '4': [types.LabeledPrice(label='Item4', amount=400000)],
    '5': [types.LabeledPrice(label='Item5', amount=500000)],
    '6': [types.LabeledPrice(label='Item6', amount=600000)]
}


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
