import telebot
import webbrowser
import sqlite3
from telebot import types
bot=telebot.TeleBot("6838471691:AAGzZ7RHuC8QS98-LAgx3zNUD8ML8eIXLEU")
age=None
height=None
ves=None
poison=None
sex=None
oper=None
chron=None
@bot.message_handler(commands=["start"])
def start(message):
        conn= sqlite3.connect("bd1.sql")
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,sex text,AGE int,HEIGHT int,VES int ,POISON text,OPER text,CHRON text)')
        conn.commit()
        cur.close()
        conn.close()
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Заполнить профиль")
        markup.row(btn1)
        bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name} {message.from_user.last_name}", reply_markup=markup)
        bot.send_message(message.chat.id, " Мы создали нашего бота ,чтобы люди могли узнать по своей истории болезни и жалобам что с ними не так ")
        bot.send_message(message.chat.id, "Поэтому вам придеться рассказть небольшие секретики о вас", )
        bot.send_message(message.chat.id, "вам необходимо заполнить профиль, для этого нажмите на кнопку'Заполнить профиль' ", )
        bot.register_next_step_handler(message,prof)
@bot.message_handler(commands=["info"])
def main(message):
    bot.send_message(message.chat.id, message)
def prof(message):
    bot.send_message(message.chat.id,"Введите свой пол:",)
    bot.register_next_step_handler(message,pol)
def pol(message):
    global sex
    sex=message.text
    bot.send_message(message.chat.id,"Хорошо,Введите свой возраст")
    bot.register_next_step_handler(message,Age)
def Age(message):
    global age
    age=message.text
    bot.send_message(message.chat.id,"Отлично,теперь введите свой рост: ")
    bot.register_next_step_handler(message, Height)
def Height(message):
    global height
    height=message.text
    bot.send_message(message.chat.id,"Замечательно, теперь введите ваш вес",)
    bot.register_next_step_handler(message,Ves)
def Ves(message):
    global ves
    ves=message.text
    bot.send_message(message.chat.id,"Введите список болезней которыми мы переболели,через запятую.\nЕсли же таких нету ,то введите 'Нет'")
    bot.register_next_step_handler(message,OPER)
def OPER(message):
    global poison
    poison=message.text
    bot.send_message(message.chat.id,"Теперь вам необходимо ввести перенесенные вами операции, через запятую.\nЕсли же таких нету ,то введите 'Нет'")
    bot.register_next_step_handler(message,CHRON)
def CHRON(message):
    global oper
    oper = message.text
    bot.send_message(message.chat.id,"Если у вас имеются хронические заболевания то введите их через запятую. \n Если же у вас их нету то введите 'Нету':",)
    bot.register_next_step_handler(message,lie)

def lie(message):
    global poison
    global age
    global height
    global ves
    global sex
    global chron
    global oper
    chron = message.text
    conn = sqlite3.connect("bd1.sql")
    cur = conn.cursor()
    cur.execute('INSERT INTO users (SEX,AGE,HEIGHT,VES,POISON,OPER,CHRON) VALUES("%s","%s","%s","%s","%s","%s","%s")' % (sex,age,height,ves,poison,oper,chron))
    conn.commit()
    cur.close()
    conn.close()
    markup = types.ReplyKeyboardMarkup()
    btn1= types.KeyboardButton("Список пользователей")
    btn2 = types.KeyboardButton("Перейти в профиль")
    btn3 = types.KeyboardButton("МЫ в соц.сетях")
    btn4 = types.KeyboardButton("Контакты горячей линии")
    btn5 = types.KeyboardButton("Клиники в городе...")
    btn6= types.KeyboardButton("Техподдрежка")
    btn7= types.KeyboardButton("Записаться на прием")
    btn8=types.KeyboardButton("Редактировать профиль")
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    markup.row(btn6,btn7)
    markup.row(btn1,btn8)
    bot.send_message(message.chat.id,f"Вот ваши данные: \nПол: {sex} \nВозраст: {age}\nРост: {height}\nВес: {ves} \nПеренесенные болезни:{poison} \nПеренесённые операции:{oper} \nХронические заболевания:{chron}",reply_markup=markup)
    bot.register_next_step_handler(message,profile)
def profile(message):
    if message.text=="МЫ в соц.сетях":
        bot.send_message(message.chat.id,"Телеграмм: https://t.me/medsigroup")
        bot.send_message(message.chat.id, "Однолассники  https://ok.ru/medsimed")
        bot.send_message(message.chat.id, "Ютуб https://www.youtube.com/user/medsiclinic")
        bot.send_message(message.chat.id, "Вконтакте https://vk.com/medsi_clinic")
    elif message.text == "Контакты горячей линии":
        bot.send_message(message.chat.id,"Москва и Московская:+7 (495) 431-70-04  \nСанкт-Петербург: (812) 336 33 33 \nБарнаул (3852) 63 68 38 \nБрянск: +7 (4832) 32-34-26\nВладикавказ: +7 (8672) 77-40-10 \nВолгоград: +7 (8442) 59-10-12 \nВыксаг: +7 (831) 773-93-03 \nИжевск: (3412) 91-20-03 \nНижневартовск:  (3466) 29-88-00 \nНягань: (34672) 5-93-40 \nПермь: (342) 2 150 630 \nРостов-на-Дону: +7 (863) 280-00-33 \nТуапсе: +7 (3412) 91-20-03 \nСаранск: +7 (8342) 37-00-70 \nУфа: +7 (347) 225-21-61")
    elif message.text=="Перейти в профиль":
        global poison
        global age
        global height
        global ves
        global sex
        global chron
        global oper
        bot.send_message(message.chat.id,f"Вот ваши данные {message.from_user.first_name} {message.from_user.last_name}:\nВаш пол:{sex} \nВозраст:{age} лет\nРост: {height} cантиметров \nВес: {ves} кг \nПеренесенные болезни: {poison}\nПеренесённые операции:{oper}\nХронические заболевания:{chron}")
    elif message.text == "Клиники в городе...":
        markup = types.InlineKeyboardMarkup(row_width=4)
        btn1=types.InlineKeyboardButton("Москва и Московскафя область",callback_data="moscow")
        btn2 = types.InlineKeyboardButton("Санкт-Петербург",callback_data="SPB")
        btn3 = types.InlineKeyboardButton("Барнаул",callback_data="barn")
        btn4 = types.InlineKeyboardButton("Брянск",callback_data="Bryansk")
        btn5 = types.InlineKeyboardButton("Владикавказ",callback_data="Vladik")
        btn6 = types.InlineKeyboardButton("Владимир",callback_data="VOVA")
        btn7 = types.InlineKeyboardButton("Волгоград",callback_data="Volg")
        btn8 = types.InlineKeyboardButton("Выкса",callback_data="viksa")
        btn9 = types.InlineKeyboardButton("Ижевск",callback_data="igevsk")
        btn10 = types.InlineKeyboardButton("Нижневартовск",callback_data="nign")
        btn11= types.InlineKeyboardButton("Нягань",callback_data="Nagan")
        btn12= types.InlineKeyboardButton("Пермь",callback_data="perm")
        btn13 = types.InlineKeyboardButton("Ростов-на-Дону",callback_data="Rostik")
        btn14 = types.InlineKeyboardButton("Туапсе",callback_data="Tuapse")
        btn15 = types.InlineKeyboardButton("Саранск",callback_data="Saransk")
        btn16= types.InlineKeyboardButton("Уфа",callback_data="Ufa")
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16)
        bot.send_message(message.chat.id,"Клиники есть в следующих городах:",reply_markup=markup)
    elif message.text == "Записаться на прием":
        markup = types.InlineKeyboardMarkup(row_width=4)
        btn1 = types.InlineKeyboardButton("Москва и Московскафя область", callback_data="moscow1")
        btn2 = types.InlineKeyboardButton("Санкт-Петербург", callback_data="SPB1")
        btn3 = types.InlineKeyboardButton("Барнаул", callback_data="barn1")
        btn4 = types.InlineKeyboardButton("Брянск", callback_data="Bryansk1")
        btn5 = types.InlineKeyboardButton("Владикавказ", callback_data="Vladik1")
        btn6 = types.InlineKeyboardButton("Владимир", callback_data="VOVA1")
        btn7 = types.InlineKeyboardButton("Волгоград", callback_data="Volg1")
        btn8 = types.InlineKeyboardButton("Выкса", callback_data="viksa1")
        btn9 = types.InlineKeyboardButton("Ижевск", callback_data="igevsk1")
        btn10 = types.InlineKeyboardButton("Нижневартовск", callback_data="nign1")
        btn11 = types.InlineKeyboardButton("Нягань", callback_data="Nagan1")
        btn12 = types.InlineKeyboardButton("Пермь", callback_data="perm1")
        btn13 = types.InlineKeyboardButton("Ростов-на-Дону", callback_data="Rostik1")
        btn14 = types.InlineKeyboardButton("Туапсе", callback_data="Tuapse1")
        btn15 = types.InlineKeyboardButton("Саранск", callback_data="Saransk1")
        btn16 = types.InlineKeyboardButton("Уфа", callback_data="Ufa1")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15,btn16)
        bot.send_message(message.chat.id, "В списке ниже представлены города в которых можно записаться на личный приём", reply_markup=markup)
    elif message.text=="Техподдрежка":
        bot.send_message(message.chat.id,"Глава проекта:https://t.me/da_robertosik | @da_robertosik \n Разработчик телеграмм-бота: https://t.me/fucking_kurwa_man | @fucking_kurwa_man \n Разработчик нейросети: https://t.me/lootally | @lootally \nОтветственные по АД: https://t.me/da_robertosik | @da_robertosik и https://t.me/dea1ler | @dea1ler \nТехподдрежка может отвечать в течение 6-9 рабочих дней")
    elif message.text == "Список пользователей":
        conn = sqlite3.connect("bd1.sql")
        cur = conn.cursor()
        cur.execute( 'SELECT * FROM users')
        us=cur.fetchall()
        inf=''
        for i in us:
            inf+= f'Возраст:{i[1]}, Рост: {i[2]}, Вес {i[3]}, История болезней:{i[4]} \n'
        bot.send_message(message.chat.id,inf)
        cur.close()
        conn.close()
    if message.text=="Редактировать профиль":
        bot.send_message(message.chat.id,"Введите свой пол:")
        bot.register_next_step_handler(message,pol1)
    bot.register_next_step_handler(message,profile)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data=="moscow":
            webbrowser.open("https://medsi.ru/clinics/")
        elif call.data == "SPB":
            webbrowser.open("https://spb.medsi.ru/clinics/")
        elif call.data == "barn":
            webbrowser.open("https://barnaul.medsi.ru/clinics/")
        elif call.data == "Bryansk":
            webbrowser.open("https://bryansk.medsi.ru/")
        elif call.data == "Vladik":
            webbrowser.open("https://vladikavkaz.medsi.ru/")
        elif call.data == "VOVA":
            webbrowser.open("https://vladimir.medsi.ru/")
        elif call.data == "Volg":
            webbrowser.open("https://volgograd.medsi.ru/clinics/")
        elif call.data == "Viksa":
            webbrowser.open("https://vyksa.medsi.ru/")
        elif call.data == "igevsk":
            webbrowser.open("https://izhevsk.medsi.ru/clinics/")
        elif call.data == "nign":
            webbrowser.open("https://nignevartovsk.medsi.ru/clinics/")
        elif call.data == "Nagan":
            webbrowser.open("https://perm.medsi.ru/clinics/")
        elif call.data == "perm":
            webbrowser.open("https://perm.medsi.ru/clinics/")
        elif call.data == "Rostik":
            webbrowser.open("https://rostov.medsi.ru/")
        elif call.data == "Tuapse":
            webbrowser.open("https://tuapse.medsi.ru/")
        elif call.data == "Saransk":
            webbrowser.open("https://saransk.medsi.ru/")
        elif call.data == "Ufa":
            webbrowser.open("https://ufa.medsi.ru/clinics/")
        elif call.data=="moscow1":
            webbrowser.open("https://medsi.ru/services/")
        elif call.data == "SPB1":
            webbrowser.open("https://spb.medsi.ru/services/")
        elif call.data == "barn1":
            webbrowser.open("https://barnaul.medsi.ru/clinics/")
        elif call.data == "Bryansk1":
            webbrowser.open("https://bryansk.medsi.ru/services/")
        elif call.data == "Vladik1":
            webbrowser.open("https://vladikavkaz.medsi.ru/")
        elif call.data == "VOVA1":
            webbrowser.open("https://vladimir.medsi.ru/")
        elif call.data == "Volg1":
            webbrowser.open("https://volgograd.medsi.ru/services/")
        elif call.data == "Viksa1":
            webbrowser.open("https://vyksa.medsi.ru/services/")
        elif call.data == "igevsk1":
            webbrowser.open("https://izhevsk.medsi.ru/services/")
        elif call.data == "nign1":
            webbrowser.open("https://izhevsk.medsi.ru/services/")
        elif call.data == "Nagan1":
            webbrowser.open("https://nyagan.medsi.ru/services/")
        elif call.data == "perm1":
            webbrowser.open("https://perm.medsi.ru/services/")
        elif call.data == "Rostik1":
            webbrowser.open("https://rostov.medsi.ru/services/")
        elif call.data == "Tuapse1":
            webbrowser.open("https://tuapse.medsi.ru/")
        elif call.data == "Saransk1":
            webbrowser.open("https://saransk.medsi.ru/")
        elif call.data == "Ufa1":
            webbrowser.open("https://ufa.medsi.ru/services/")
def pol1(message):
    global sex
    sex = message.text
    bot.send_message(message.chat.id, "Хорошо,Введите свой возраст")
    bot.register_next_step_handler(message, Age1)

def Age1(message):
    global age
    age = message.text
    bot.send_message(message.chat.id, "Отлично,теперь введите свой рост: ")
    bot.register_next_step_handler(message, Height1)

def Height1(message):
    global height
    height = message.text
    bot.send_message(message.chat.id, "Замечательно, теперь введите ваш вес", )
    bot.register_next_step_handler(message, Ves1)

def Ves1(message):
    global ves
    ves = message.text
    bot.send_message(message.chat.id,"Введите список болезней которыми мы переболели,через запятую.\nЕсли же таких нету ,то введите 'Нет'")
    bot.register_next_step_handler(message, OPER1)

def OPER1(message):
     global poison
     poison = message.text
     bot.send_message(message.chat.id, "Теперь вам необходимо ввести перенесенные вами операции, через запятую:")
     bot.register_next_step_handler(message, CHRON1)

def CHRON1(message):
     global oper
     oper = message.text
     bot.send_message(message.chat.id,"Если у вас имеются хронические заболевания то введите их через запятую. \n Если же у вас их нету то введите 'Нету':", )
     bot.register_next_step_handler(message, lie1)

def lie1(message):
     global poison
     global age
     global height
     global ves
     global sex
     global chron
     global oper
     chron = message.text
     conn = sqlite3.connect("bd1.sql")
     cur = conn.cursor()
     cur.execute('INSERT INTO users (SEX,AGE,HEIGHT,VES,POISON,OPER,CHRON) VALUES("%s","%s","%s","%s","%s","%s","%s")' % (sex, age, height, ves, poison, oper, chron))
     conn.commit()
     cur.close()
     conn.close()
     bot.send_message(message.chat.id,f"Вот ваши данные: \nПол: {sex} \nВозраст: {age}\nРост: {height}\nВес: {ves} \nПеренесенные болезни:{poison} \nПеренесённые операции:{oper} \nХронические заболевания:{chron}")
bot.infinity_polling()