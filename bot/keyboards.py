from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

webapp = WebAppInfo(url='https://bunyodnaimov.github.io/aiogram_web_app.github.io/')

site_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Site', web_app=webapp)],
], resize_keyboard=True)
