from aiogram import types, Dispatcher, F

from aiogram.filters import CommandStart, Command

from keyboards import site_kb
from db import db_get_all_products

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom", reply_markup=site_kb)


@dp.message(Command(commands='products'))
async def cmd_products(message: types.Message):
    products = db_get_all_products()
    for product in products:
        await message.answer(text=f"Product {product[1]}\n"
                                  f"Prise {product[3]}")


@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_item_btn(msg: types.Message):
    await msg.answer(f"Вы выбрали товар {msg.web_app_data.data}!")
