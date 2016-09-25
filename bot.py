import socket
import string
import re
from time import sleep
import threading

# Переменные
HOST = "irc.chat.twitch.tv"
NICK = "nyargh_bot"
PORT = 6667
PASS = "oauth:vjc7im13otek7lbyfdh9gnieryschz"
readbuffer = ""
MODT = False
CHAN = "#sum174"
RATE = (20/30)
TTL = 150

# Отправка сообщения
def Send_message(message):
    messagetos = "PRIVMSG " + CHAN + " :" + message + "\r\n"
    s.send(messagetos.encode("utf-8"))
    sleep(RATE)

#Реклама
def spam():
    num = 1
    while num < 10:
        print("SPAM STARTED")
        Send_message("Заходите и вступайте в мою группу в ВК: https://vk.com/sum174 Вас ждут игровые новости, анонсы стримов, адекватная компания и общение)")
        sleep(TTL)
        Send_message("Хочешь чтобы твоя музыка прозвучала на стриме? Тебе сюда: https://vk.com/topic-106351984_34231605")
        sleep(TTL)
        Send_message("Поддержать ламповое настроение монеткой: http://www.donationalerts.ru/r/sum174 альтернатива: https://twitch.streamlabs.com/Sum174")
        sleep(TTL)
        Send_message("Подпишись,будь плюшевой пандой!")
        sleep(TTL)
        Send_message("Как долго уже идет стрим? Узнай с помощью команды: !time")
        sleep(TTL)
        print("SPAM DONE")

#Пинг-Понг
def ppong(response):
    print("PONG STARTED")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv".encode("utf-8"))
        print("PONG")
        sleep(5)

if __name__ == '__main__':
    print("BOT STARTED")
    print("Trying to connect to: " + CHAN + " with: " + NICK)
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
    Send_message("О, кажется, меня правильно настроили!) Берусь за работу!) Всем Привет)")
    print("BOT CONNECTED")
    while True:
        response = s.recv(1024).decode("utf-8")
        t1 = threading.Thread(ppong(response))
        t2 = threading.Thread(spam())
        t1.start()
        t2.start()
        t1.join()
        t2.join()