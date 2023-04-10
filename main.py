import telebot
import requests
import random
import yaml
from telebot import types
from time import sleep
#from pprint import pprint

bot = telebot.TeleBot('TOKENNNNN')

@bot.message_handler(commands=["start"])
def start(m, res=False):

    num=0
    if (str(m.chat.type)=="group"):
        with open('ALL_GROUPS.yaml') as f:
            templates = yaml.safe_load(f)
        base = [{"Number": (len(templates)) + 1, "id": m.chat.id, "Title": m.chat.title}]

        for i in range(len(templates)):
            if (int(m.chat.id) == int(templates[i]["id"])):
                num = 1 + num
                break
        if (num == 0):
            with open('ALL_GROUPS.yaml', 'w') as f:
                documents = yaml.dump(templates, f)
                documents = yaml.dump(base, f)
    else:
        with open('ALL_USERS.yaml') as f:
            templates = yaml.safe_load(f)
        base = [{"Number": (len(templates)) + 1, "id": m.from_user.id, "username": m.from_user.username,
                 "first_name": m.from_user.first_name}]
        for i in range(len(templates)):
            if (int(m.from_user.id) == int(templates[i]["id"])):
                num = 1 + num
                break
        if (num == 0):
            with open('ALL_USERS.yaml', 'w') as f:
                documents = yaml.dump(templates, f)
                documents = yaml.dump(base, f)



    bot.send_message(m.chat.id, 'Напиши /help Чтобы узнать что я умею))')
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Inst", url='https://www.instagram.com/valentin_vffv2000/')
    markup.add(button1)
    bot.send_message(m.chat.id,
                     "Привет, {0.first_name}! Меня написал вот этот чел @vffv2000)".format(m.from_user),
                     reply_markup=markup)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup1.add(btn1, btn2)
    #bot.send_message(m.chat.id,text="".format(m.from_user), reply_markup=markup1)


@bot.message_handler(commands=["help"])
def help(message, res=False):
    bot.send_message(message.chat.id, text="Показывать погоду (/weather)\n"
                                           "Показать твой id (/id)\n"
                                           "Показать картинку котика (/cat)\n"
                                           "Показать картинку собаки (/dog)\n"
                                           "Показать интересный факт про число (/fact)")


@bot.message_handler(commands=["cat"])
def cat(m,res=False):
    num=random.randint(1, 1000)
    source = requests.get(f"https://aws.random.cat/view/{num}").text
    if "id=\"cat" in source:
        res=str(source.split("src=\"")[1].split("\"")[0])
        bot.send_message(m.chat.id, res)
    else:
        bot.send_message(m.chat.id, "Картинки закончились. Попробуй снова)")


@bot.message_handler(commands=["dog"])
def cat(m,res=False):
    source = requests.get(f"https://random.dog/woof.json").text
    index=source.find("url")
    bot.send_message(m.chat.id, source[index+6:-2])


@bot.message_handler(commands=["fact"])
def fact(m,res=False):
    number=random.randint(1, 9999)
    url = 'http://numbersapi.com/{}/math'.format(number)
    res = requests.get(url, params={'lang': 'ru' }).text
    if ("is a boring" in res) or ("is an uninteresting" in res) or ("is an unremarkable" in res) or ("is a number for which " in res):
        fact(m)
    else:
        bot.send_message(m.chat.id, res)


@bot.message_handler(commands=["1weather1"])
def weather(m,s_city, res=False):
    if (s_city==""):
        bot.send_message(m.chat.id, "Введите /weather Minsk или любой другой город " )
    city_id = 0
    appid = "4dbc9b8bce7411705a58d5a4a39c3186"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        bot.send_message(m.chat.id, "Город:" +str(data["name"])+"\n"
                         "Погодные условия: " + str(data['weather'][0]['description'])+"\n"
                                                                    )
        bot.send_message(m.chat.id, "Температура за окном: " + str(data['main']['temp'])+"\n"+
                                                                                         "А ощущается как "+str(data["main"]["feels_like"]))
    except Exception as e:
        print("Exception (weather):", e)
        pass
   #vremya(m, s_city)


@bot.message_handler(commands=["id"])
def id_k(message, res=False, base=None):
    bot.send_message(message.chat.id,'Ваш ID: '+ str(message.from_user.id))
    print(str(message.from_user.id) + " " + str(message.from_user.username))



@bot.message_handler(content_types=["text"])
def handle_text(message):

    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        btn3_weather = types.KeyboardButton("/weather")

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,btn3_weather, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
    elif message.text == "Что я могу?":
        help(message)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif ("/weather" in message.text):
        s_city=message.text[9:]
        weather(message,s_city)
    elif("/Ahelp" in message.text):
        admin=False
        admin=Admin_check(message)
        if (admin==True):
            bot.send_message(message.chat.id, "Команды для админов:\n"
                                              "/spam-рассылка сообщений\n"
                                              "/show Показать данные всех участников бота))")
        else:
            bot.send_message(message.chat.id, "Вы не администратор")
    elif ("/show" in message.text):
        admin = False
        admin = Admin_check(message)
        if (admin == True):
            bot.send_message(message.chat.id, "Вы лучший администратор))")
            bot.send_message(message.chat.id, "Выполняется комаанда " + message.text)
            with open('ALL_USERS.yaml') as f:
                templates = yaml.safe_load(f)
                for i in range(len(templates)):
                    bot.send_message(message.chat.id,"Number: "+str(templates[i]["Number"])+"\n"
                                                      "first_name: "+str(templates[i]["first_name"])+"\n"
                                                      "id: "+str(templates[i]["id"])+"\n"                          
                                                      "username: "+str(templates[i]["username"])                                           )
        else:
            bot.send_message(message.chat.id, "Вы не администратор")
    elif ("/spam" in message.text):
        admin = False
        admin = Admin_check(message)

        if (admin == True):
            bot.send_message(message.chat.id, "Выполняется команда "+message.text[:6])
            with open('ALL_USERS.yaml') as f:
                templates = yaml.safe_load(f)
                for i in range(len(templates)):
                    bot.send_message(templates[i]['id'],  message.text[6:])
            with open('ALL_GROUPS.yaml') as f:
                templates = yaml.safe_load(f)
                for i in range(len(templates)):
                    bot.send_message(templates[i]['id'],  message.text[6:])
        else:
            bot.send_message(message.chat.id, "Вы не администратор")

def vremya(message,s_city):
    sleep(5)
    weather(message,s_city)
    vremya(message,s_city)#для зациклвания функции с временем в сек


def Admin_check(message):

    with open('ADMIN.yaml') as f:
        templates = yaml.safe_load(f)
    for i in range(len(templates)):
        if (int(message.from_user.id) == int(templates[i]["id"])):
            admin = True
            return admin


bot.polling(none_stop=True, interval=0)
