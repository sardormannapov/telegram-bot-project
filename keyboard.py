from telebot import types
from language.bot_lang import *
from language.keyboard_lang import *


def generate_main_menu(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_computer_mice = types.KeyboardButton(text=mouce_keyboard[lang])
    keyboard.row(btn_computer_mice)
    return keyboard


def generate_inline_url(url, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text=more_keyboard[lang], url=url)
    btn_more_bay = types.InlineKeyboardButton(text=buy_keyboard[lang], callback_data="buy")
    keyboard.row(btn_more_bay, btn_more)
    return keyboard



def generate_url(url, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text=more_keyboard[lang], url=url)
    keyboard.row(btn_more)
    return keyboard



def generate_pagination(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_next = types.KeyboardButton(text=next_keyboard[lang])
    btn_prev = types.KeyboardButton(text=back_keyboard[lang])
    btn_menu = types.KeyboardButton(text=back_to_menu[lang])
    keyboard.row(btn_prev, btn_next)
    keyboard.row(btn_menu)
    return keyboard



def generate_language():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_uz = types.KeyboardButton(text="🇺🇿UZ")
    btn_ru = types.KeyboardButton(text="🇷🇺RU")
    keyboard.row(btn_uz, btn_ru)
    return keyboard




















