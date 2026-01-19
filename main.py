from telebot import types
import telebot

bot = telebot.TeleBot('8279809165:AAG_kJWt9hT2tmLgGsKN1Xpgn8Jd4WfEaFY')

# Создаем меню с Reply-кнопками
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn1 = types.KeyboardButton('🌐 Сайт')
    btn2 = types.KeyboardButton('📅 Расписание')
    btn3 = types.KeyboardButton('📞 Контакты')
    btn4 = types.KeyboardButton('ℹ️ О нас')
    btn5 = types.KeyboardButton('🔙 Главное меню')
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, '🏫 *МКЭиИТ*\nВыберите раздел:', 
                     parse_mode='Markdown', reply_markup=markup)

# Обработка текстовых сообщений (нажатий на кнопки)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '🌐 Сайт':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com')
        markup.add(btn)
        bot.send_message(message.chat.id, '🌐 *Официальный сайт GitHub*', 
                         parse_mode='Markdown', reply_markup=markup)
    
    elif message.text == '📅 Расписание':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Открыть расписание', url='https://mkeiit.ru/?page_id=2699')
        markup.add(btn)
        bot.send_message(message.chat.id, '📅 *Расписание занятий*', 
                         parse_mode='Markdown', reply_markup=markup)
    
    elif message.text == '📞 Контакты':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Контакты', url='https://www.exploit-db.com/google-hacking-database')
        markup.add(btn)
        bot.send_message(message.chat.id, '📞 *hacking database*', 
                         parse_mode='Markdown', reply_markup=markup)
    
    elif message.text == 'ℹ️ О нас':
        bot.send_message(message.chat.id, 
                         'ℹ️ *О НАС*\n\nИДИ НАХУЙ', 
                         parse_mode='Markdown')
    
    elif message.text == '🔙 Главное меню':
        # Пересоздаем главное меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('🌐 Сайт')
        btn2 = types.KeyboardButton('📅 Расписание')
        btn3 = types.KeyboardButton('📞 Контакты')
        btn4 = types.KeyboardButton('ℹ️ О нас')
        btn5 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        
        bot.send_message(message.chat.id, '🏫 *Главное меню МКЭиИТ*', 
                         parse_mode='Markdown', reply_markup=markup)
    
    else:
        bot.send_message(message.chat.id, 'Используйте кнопки меню для навигации')

if __name__ == '__main__':
    bot.polling(none_stop=True)