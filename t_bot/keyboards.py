from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

webapp = WebAppInfo(url='https://8e3d-178-218-201-42.ngrok-free.app')

site_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Site', web_app=webapp)],
], resize_keyboard=True)
