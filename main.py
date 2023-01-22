import telebot
from telebot import types

bot = telebot.TeleBot('5859947490:AAGi869_UulnDH1qRNj5tILrxhB_bds7Bkw')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    back = types.KeyboardButton(text='🔙Назад')
    menu = types.KeyboardButton(text='🏠Главное меню🏠')
    clear = types.KeyboardButton(text='🧹Очистить чат')
    keyboard_menu.add(menu, back)

    # mess =
    bot.send_message(message.chat.id, '<b>Йоу, мы занимаемся доставкой оригинальной продукции '
                                      'всех самых популярных брендов: Nike, Adidas, Jordan, Gucci, '
                                      'Balenciaga и др. - с магазина Poizon. При нынешних ограничениях '
                                      'достать оригинальный товар проблематично, поэтому мы предоставляем '
                                      'свои услуги по низким ценам. Если удалось тебя заинтересавать,'
                                      ' обязательно смотри FAQ перед заказом</b>',
                     parse_mode='html', reply_markup=keyboard_menu)

    # кнопки FAQ и Сделать заказ
    markup = types.InlineKeyboardMarkup()
    FAQ = types.InlineKeyboardButton(text='🆘FAQ🆘', callback_data="faq")
    BUY = types.InlineKeyboardButton(text='🚛Сделать заказ', callback_data="buy")
    markup.add(FAQ, BUY)

    photo = open('poizon.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    if call.message:
        bot.answer_callback_query(callback_query_id=call.id)
        message1_id = None
        message2_id = None

        if call.data == "faq":
            list1 = types.InlineKeyboardMarkup()
            BUY = types.InlineKeyboardButton("🚛Сделать заказ", callback_data="buy")
            list1.add(BUY)
            bot.send_message(call.message.chat.id,
                             text='<b>Часто задаваемые вопросы\n'
                                  '\n'
                                  '1.	Что такое POIZON и зачем заказывать из Китая?</b>\n'
                                  'POIZON(DeWu)- китайский магазин ОРИГИНАЛЬНЫХ брендов. '
                                  'При нынешних введенных ограничениях, это звучит очень интересно,'
                                  ' а учитывая стоимость, которая НИЖЕ чем в РФ НА 30-40%, и огромный ассортимент, '
                                  'тебе вообще захочется оставить там всю свою зп. POIZON -  это аналог русского OZON или WB, '
                                  'но только с намного большим выбором – оно и понятно, узкоглазые быстро размножаются. '
                                  'На этой платформе возможно купить фактически что угодно – хоть то будет пара носков '
                                  'или же Lamborghini за каких-то ~60 лимонов. Наиболее популярные категории среди РФ '
                                  'покупателей: одежда, обувь, техника - доставку этих товаров мы Вам и предлагаем.\n'
                                  '\n'
                                  '<b>2.	Почему я не могу сделать заказ сам?</b>\n'
                                  'Чтобы сделать заказ на платформе POIZON, необходимо:\n'
                                  '1)Наличие китайской карты для оплаты – удачи ее открыть)\n'
                                  '2)Денежные средства на этой же карте в валюте CNY – обменники берут большую комиссию при переводе денег\n'
                                  '3)Транспортировка по Китаю до склада отправки в РФ\n'
                                  '4)Поиск оптимальной транспортной компании, чтобы твои тапки дошли в РФ быстро, и ты при этом потратил бы меньше денег.\n'
                                  '5)Транспортировка по РФ до места выдачи\n'
                                  'Чтобы сэкономить Ваше время и деньги, мы и предлагаем свои услуги\n'
                                  '\n'
                                  '<b>3.	Стоимость и сроки доставки\n</b>'
                                  'Мы уже позаботились за Вас о поиске транспортных компаний, а также об оплате покупки. Заказывая у нас, ты совместишь низкую цену с быстрой доставкой\n'
                                  '•	Стоимость рассчитывается из:\n'
                                  'стоимость товара в CNY * НЫНЕШНИЙ курс\n'
                                  'доставка товара в РФ(600руб за 0.5кг) + доставка по РФ\n'
                                  'плата в размере 10% от стоимости заказа за нашу работу\n'
                                  '•	Средние сроки доставки* до клиента 3-4 недели, но обычно это занимает не более месяца\n'
                                  '*Сроки могут корректироваться, уточняйте при оформлении заказа',
                             parse_mode='html', reply_markup=list1)

        if call.data == "buy":
            list2 = types.InlineKeyboardMarkup(row_width=1)
            download = types.InlineKeyboardButton("🔃Скачать Poizon", callback_data="download")
            help_button = types.InlineKeyboardButton("👙Помощь в подборе товара",
                                                     url="https://t.me/kulik_kov")
            price = types.InlineKeyboardButton("💵Наши цены", callback_data="price")
            write_button = types.InlineKeyboardButton("💰Сделать заказ",
                                                      callback_data="write")
            list2.add(download, help_button, price, write_button)
            bot.send_message(call.message.chat.id, text='Если ты дошел до этого этапа, назад пути нет',
                             reply_markup=list2)

        if call.data == "download":
            list3 = types.InlineKeyboardMarkup(row_width=1)
            url_button_ios = types.InlineKeyboardButton("Скачать для IOS📱",
                                                        url="https://apps.apple.com/ru/app/得物-有毒的运动-潮流-好物/id1012871328")
            url_button_android = types.InlineKeyboardButton("Скачать для Android🤖",
                                                            url="https://apkpure.com/ru/poizon-authentic-fashion/com.shizhuang.poizon.hk")
            back_button = types.InlineKeyboardButton("🔙Вернуться", callback_data='buy')
            list3.add(url_button_ios, url_button_android, back_button)
            bot.send_message(call.message.chat.id, text='Скачать приложение:', reply_markup=list3)
            bot.delete_message(call.message.chat.id, call.message.message_id)

        if call.data == "price":
            list4 = types.InlineKeyboardMarkup(row_width=1)
            write_button = types.InlineKeyboardButton("💰Сделать заказ",
                                                      callback_data="write")
            back_button = types.InlineKeyboardButton("🔙Вернуться", callback_data='buy')
            list4.add(write_button, back_button)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text='Стоимость рассчитывается из:\n'
                                                                      '1)стоимость товара в CNY * НЫНЕШНИЙ курс\n'
                                                                      '2)доставка товара в РФ(600руб за 0.5кг) + доставка по РФ\n'
                                                                      '3)плата в размере 10% от стоимости заказа за нашу работу\n',
                                           reply_markup=list4)

        if call.data == "write":
            list5 = types.InlineKeyboardMarkup(row_width=1)
            write_button = types.InlineKeyboardButton("💰Заказать/Где мои money, bitch💰",
                                                      url="https://t.me/kulik_kov")
            list5.add(write_button)

            photo = open('size.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo,
                           caption='Пример оформления заказа:\n'
                                   '【得物】得物er-4B6V0J2G发现一件好物，œAP3mz4Xœ '
                                   'https://dw4.co/t/A/12dtbYgY adidas originals '
                                   'Forum 84 Low 耐磨复古 低帮休闲板鞋 男女同款 粉红,9.4万+人想要\n'
                                   'размер - 38RF\n'
                                   '\n'
                                   'Главное, чтобы вы отправили ссылку на товар '
                                   'и правильно указанный размер. Размер, советуем смотреть '
                                   'по длине стельки в см. Как найти таблицу размеров, '
                                   'указано на фото',
                           parse_mode='html', reply_markup=list5)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == '🏠Главное меню🏠':
        bot.send_message(message.chat.id, text='/start', parse_mode='html')

    if message.text == '🔙Назад':
        bot.delete_message(message.chat.id, message.message_id - 1)

    #if message.text == '🧹Очистить чат':


bot.polling(none_stop=True)
