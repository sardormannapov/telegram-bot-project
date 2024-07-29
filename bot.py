import telebot
import time
from main import Postgres
from telebot.types import LabeledPrice
from keyboard import *
from language.bot_lang import *
import os
user_langs = {}



token = os.getenv("TOKEN")
click_token = os.getenv("CLICK_TOKEN")

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start"])

def start(message):
    chat_id = message.chat.id
    lang = bot.send_message(chat_id, "Выберите язык!", reply_markup=generate_language())
    bot.register_next_step_handler(lang, menu)


def menu(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id),
    if message.text == "🇺🇿UZ":
        lang = "uz"
        bot.send_photo(chat_id, 'https://olcha.uz/image/original/sliders/oz/cdn_1/2024-05-07/ATdXA0eMIH0wwYQwvRcgnLczlqq4Vli8ppOmEsQIDqLAzyBI0AQO7AtxKXxH.jpg',
                   caption=caption[lang], reply_markup=generate_url("https://olcha.uz/ru/category/noutbuki-planshety-kompyutery", lang))


    if message.text == "🇷🇺RU":
        lang = "ru"
        bot.send_photo(chat_id, 'https://olcha.uz/image/original/sliders/oz/cdn_1/2024-05-07/ATdXA0eMIH0wwYQwvRcgnLczlqq4Vli8ppOmEsQIDqLAzyBI0AQO7AtxKXxH.jpg',
                   caption=caption[lang], reply_markup=generate_url("https://olcha.uz/ru/category/noutbuki-planshety-kompyutery", lang))

    catalog = bot.send_message(chat_id, catalog_lang[lang], reply_markup=generate_main_menu(lang))
    bot.register_next_step_handler(catalog, main_catalogs)
    user_langs[chat_id] = lang



def main_catalogs(message, product_id=0, products=None):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id)
    if message.text == back_to_menu[lang]:
        return menu(message)

    if message.text == mouce_keyboard[lang]:
        products = Postgres().select_data()


    if message.text == next_keyboard[lang] and product_id < len(products):
        product_id += 1

    elif message.text == back_keyboard[lang] and product_id > 0:
        product_id -= 1

    product = products[product_id]
    product_title = product[0]
    photo = product[1]
    product_price = product[2]
    product_url = product[3]
    bot.send_photo(chat_id, photo, caption=f'{name_product_lang[lang]} : {product_title}\n\n'
                                           f'{product_price_lang[lang]} : {product_price}'
                                           ,
                   reply_markup=generate_inline_url(product_url, lang))

    user_message = bot.send_message(chat_id, f"{quantity_in_stock_lang[lang]} : {len(products) - (product_id + 1)}",
                                    reply_markup=generate_pagination(lang))

    if message.text == next_keyboard[lang] and len(products) - (product_id + 1) == 0:
        bot.send_message(chat_id, tugadi_lang[lang])
        product_id = product_id - len(products)  # -1
    bot.register_next_step_handler(user_message, main_catalogs, product_id, products)




@bot.callback_query_handler(func=lambda call: True)
def payments(call):
     chat_id = call.message.chat.id
     product_price_data = ''
     if call.data == "buy":
         product_info = call.message.caption
         product = product_info.split(':')
         product_name = product[1].replace("Mahsulot xarakteristikasi", "")
         description = product[2]
         product_price = product[-1].replace('UZS', "")
         for x in product_price:
             if x.isdigit():
                 product_price_data += x

         INVOICE = {
             "title": product_name,
             "description": description,
             "invoice_payload": "bot-defined invoice payload",
             "provider_token": click_token,
             "start_parameter": "pay",
             "currency": "UZS",
             "prices": [LabeledPrice(label=product_name, amount=int(product_price_data + '00'))]
         }

         bot.send_invoice(chat_id, **INVOICE)
         bot.register_next_step_handler(call.message, successful_payment)


@bot.pre_checkout_query_handler(func=lambda query: True)
def invoice_checkout(query):
     """ Проверка чека """
     bot.answer_pre_checkout_query(query.id, ok=True, error_message="Ошибка оплаты !")


def successful_payment(message):
     """ Отправить сообщение о успешной оплате """
     bot.send_message(message.chat.id, "To'lov muvoffaqiyatli amalga oshirildi!")
     return menu(message)


bot.polling(none_stop=True)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        




























































