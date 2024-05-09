from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

webapp = WebAppInfo(url='https://4e88-84-54-92-97.ngrok-free.app')

site_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Site', web_app=webapp)],
], resize_keyboard=True)
