import random
import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN_HERE')


answers = [
    'Я не зрозумів, що ти хочеш сказати.',
    'Вибач, я тебе не розумію.',
    'Я не знаю такої команди.',
    'Мій розробник не говорив, що відповідати в такій ситуації... >_<'
]


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🏠 Орендувати житло')
    button2 = types.KeyboardButton('⚙️ F.A.Q')
    button3 = types.KeyboardButton('📄 Довідка')

    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        # Send a welcome message
        bot.send_message(
            message.chat.id,
            f'Привіт, {message.from_user.first_name}!\n'
            f'Ласкаво просимо до Luxury RealEstate Agency! За допомогою нашого сервісу ти можеш знайти та орендувати своє ідеальне житло.\n'
            f'Контакт з нашим агентом: https://t.me/@femalebodyinspect0r',
            reply_markup=markup
        )
    else:
        bot.send_message(message.chat.id, 'Перекинув тебе у головне меню! Вибирай!', reply_markup=markup)


# Handler for receiving photos
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'Розробник не добавив можливості переглядати фото...')



@bot.message_handler()
def info(message):
    if message.text == '🏠 Орендувати житло':
        show_properties(message)
    elif message.text == '⚙️ F.A.Q':
        show_faq(message)
    elif message.text == '📄 Довідка':
        show_help(message)
    elif message.text in ['Пентхаус', 'Квартира', 'Будинок', 'Коттедж']:
        show_property_details(message)
    elif message.text == '⚙️ Про нас':
        bot.send_message(message.chat.id, 'Агенція Luxury RealEstate Agency - підбере комфортну оселю вам та вашій родині!')
    elif message.text == '⚙️ Наша команда':
        bot.send_message(message.chat.id, 'У нас працює команда професіоналів, які допоможуть вам знайти ідеальне житло.')
    elif message.text == '💳 Оформити замовлення' or message.text == '✏️ Написати розробнику':
        webbrowser.open('https://t.me/foodeliveryy')
    elif message.text == '↩️ Назад':
        show_properties(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, random.choice(answers))


def show_properties(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Пентхаус')
    button2 = types.KeyboardButton('Квартира')
    button3 = types.KeyboardButton('Будинок')
    button4 = types.KeyboardButton('Коттедж')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    bot.send_message(message.chat.id, 'Ось усі варіанти житла, яке зараз доступне для оренди:', reply_markup=markup)


def show_property_details(message):

    properties = {
        'Пентхаус': {
            'file': './penthouse.jpg',
            'details': (
                'Пентхаус на Печерську, Розкішний пентхаус з панорамним видом на Київ і Дніпро.\n'
                'Характеристики:\n'
                'Площа: 250 кв. м\n'
                'Кімнати: 4 (3 спальні, вітальня)\n'
                'Санвузли: 3\n'
                'Кухня: сучасна техніка\n'
                'Інтер\'єр: дизайнерський ремонт\n'
                'Тераса: з барбекю та джакузі\n'
                'Зручності: паркінг, охорона, «розумний дім», спортзал, басейн\n'
                'Ціна: 5000 USD на місяць'
            )
        },
        'Квартира': {
            'file': './apartament.jpg',
            'details': (
                'Квартира для оренди на Печерську, Адреса: вул. Маккейна Джона, 7, ЖК "Французький квартал-2"\n'
                'Площа: 98 м²\n'
                'Кімнати: 3\n'
                'Поверх: 7 з 24\n'
                'Ціна: 79,230 грн/міс\n'
                'Особливості: Сучасний дизайнерський ремонт, Кухня-студія, Охоронювана територія, Поруч метро та ТРЦ'
            )
        },
        'Будинок': {
            'file': './house.jpg',
            'details': (
                'Будинок для оренди на Печерську, Адреса: вул. Євгена Коновальця, 36Е\n'
                'Площа: 200 м²\n'
                'Кімнати: 4\n'
                'Ціна: 166,800 грн/міс\n'
                'Особливості: Сучасний дизайнерський ремонт, Простора вітальня, кухня та спальні,\n'
                'Велика тераса з чудовим видом, Престижний район, поруч метро'
            )
        },
        'Коттедж': {
            'file': './cottage.jpg',
            'details': (
                'Котедж для оренди в Києві, Адреса: вул. Садова, 15\n'
                'Площа: 300 м²\n'
                'Кімнати: 5\n'
                'Ціна: 100,000 грн/міс\n'
                'Особливості: Сучасний ремонт, мебльований, Простора кухня та вітальня,\n'
                'Велика тераса та приватний сад, Паркінг на 2 авто, Тихий район, поруч з парком'
            )
        }
    }

    property_info = properties.get(message.text)
    if property_info:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Оформити замовлення')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file = open(property_info['file'], 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)
        bot.send_message(message.chat.id, property_info['details'], reply_markup=markup)


def show_faq(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('⚙️ Про нас')
    button2 = types.KeyboardButton('⚙️ Наша команда')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Розділ налаштувань.\nВиберіть один з варіантів:', reply_markup=markup)


def show_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написати розробнику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Розділ довідки. Тут ти можеш написати нашому агенту.', reply_markup=markup)


bot.polling(none_stop=True)
