### Bot Amino V1.2 by CamilaTokisaki and enchart

import amino
import random
import time
import threading
from threading import Thread

client = amino.Client()
client.login(email="тут пишите логин от аккаунта где будет бот", password="тут пишите пароль от аккаунта где будет бот")
sub_client = amino.SubClient(comId='10349519', profile=client.profile)
reloadTime = time.time() + 120

@client.callbacks.event("on_text_message")
def on_text_message(data):
        chatId = data.message.chatId
        nickname = data.message.author.nickname
        content = data.message.content
        id = data.message.messageId
        print(nickname, content)

        lis = ['Думаю что да', 'Думаю что нет', 'Наверное', 'Уверена на Все 100%',
         'Точно нет', 'Да, почему бы и нет?', 'Скорее всего да, а хотя может и нет...', 'Я не знаю ответа на этот вопрос, я глупая',
         'Почему ты так думаешь?', 'Я не уверена что тебе стоит знать ответ на твой вопрос','Нет','Да']

        lis2 = ['Извини пожалуйста', 'Прости меня дуру!', 'Прости Сэнпай, я не хотела ранить твои чувства',
          'Ты лучший человек которого я видела!']

        lis3 = ['*обняла в ответ* спасибо, мне очень приятно что ты заботишься о мне~', 'Ня~ Как приятно~', '*обняла в ответ* Не отпускай меня...', '*обняла в ответ* Можно нам так стоять вместе вечно?..', '*обняла в ответ* Я люблю тебя..', '*обняла в ответ* :3', '*обняла в ответ* я счастлива~']
        content = str(content).split(" ")

        if content[0] == "ram":
            sub_client.send_message(message="Привет! Я Рам, чем могу быть полезна?", chatId=chatId)

        if content[0] == "рам,":
            sub_client.send_message(message=str(random.choice(lis)), chatId=chatId, replyTo=id)

        if content[0] == "эй!":
            sub_client.send_message(message=str(random.choice(lis2)), chatId=chatId, replyTo=id)

        if content[0] == "love":
            sub_client.send_message(message="Я тоже люблю тебя", chatId=chatId, replyTo=id)

        if content[0] == "!love":
            mentions = data.message.extensions.get('mentionedArray')
            if mentions != None and len(mentions) == 2:
                pidorasi = [sub_client.get_user_info(x['uid']).nickname for x in mentions]
                sub_client.send_message(
                    message=f"Вероятность того, что {pidorasi[0]} и {pidorasi[1]} любят друг друга {random.randint(0, 100)}%",
                    chatId=chatId, replyTo=id)

        if content[0] == "надоели!":
            sub_client.send_message(message="Хватит Ругаться! Вы даже мне уже надоели, А я на секундочку бот!", chatId=chatId)

        if content[0] == "*обнять*":
            sub_client.send_message(message=str(random.choice(lis3)), chatId=chatId, replyTo=id)

        if content[0] == "help":
            sub_client.send_message(message="""
[B]Команды: 
adhelp-админ панель
рам,-спросить Ram
*обнять*-обнять рам
действие-взаимодействие с другими участниками
надоели!-злая Ram
эй!-попросить Rам извиниться
ram-приветствие Ram
love-признаться Ram
!love-на сколько процентов один любит другого
info-информация о обновлении
info_bot-создатели Ram
""",chatId=chatId, replyTo=id)

        if content[0] == "действия":
            sub_client.send_message(message='''
[B]Действия:
.cuddle-Прижаться
.feed-Покормить
.hug-Обнять
.kiss-Поцеловать
.pat-Погладить
.poke-Тыкнуть
.slap-ударить
.tickle-Пощекотать
.kus-делать кусь
''', chatId=chatId)

        if content[0] == ".tickle":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} щекочет {author2}', chatId=chatId)

        if content[0] == ".slap":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} бьёт {author2}', chatId=chatId)

        if content[0] == ".poke":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} тыкает в {author2}', chatId=chatId)

        if content[0] == ".pat":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} гладит {author2}', chatId=chatId)

        if content[0] == ".hug":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} обнимает {author2}', chatId=chatId)

        if content[0] == ".feed":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} Кормит {author2}', chatId=chatId)

        if content[0] == ".cuddle":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} прижимается к {author2}', chatId=chatId)

        if content[0] == ".kiss":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} целует {author2}', chatId=chatId)

        if content[0] == ".kus":
            author2 = data.message.content.split("@")[1].replace("@", "")[0:50]
            sub_client.send_message(message=f'{data.message.author.nickname} делает кусь {author2}', chatId=chatId)

        if content[0] == "привет!":
            sub_client.send_message(message="И тебе привет!", chatId=chatId, replyTo=id)

        if content[0] == "info":
            sub_client.send_message(message='''
[B]Обновления: 1.2 (дополнение)

1. Добавлена функция "действия"
2. Приветствие новых людей в сообществе

[B]Удалено:

1. Функция "game" из за ненадобности
''', chatId=chatId)
        if content[0] == "info_bot":
            sub_client.send_message(message='''
Версия бота 1.2

Создатели: 



Дискорд:

CamilaTokisaki#9903
enchart

Вк:

https://vk.com/violetta_bowten
            ''', chatId=chatId, replyTo=id)

# Дальше идёт админ панель с командами для админов, если у бота есть звание Лидера то убирайте решотки с всех строк от 150 и до 169
#        if data.message.author.role != 0:
#            if content[0] == "adhelp":
#                sub_client.send_message(message="""
#[B]Админ Панель
#morn-пожелать доброе утро
#night-пожелать спокойной ночи
#зачистка-удаленить 10 сообщений
#""", chatId=chatId, replyTo=id)
#        if content[0] == "night":
#            sub_client.send_message(message="*зевая* Спокойной ночи сладкие мои~", chatId="fdfaad0b-99d6-426c-b942-61e4c01fadfb")
#        if content[0] == "morn":
#            sub_client.send_message(message="*потираея сонные глазки улыбаясь* Доброе утро лапочки~", chatId="fdfaad0b-99d6-426c-b942-61e4c01fadfb")

#        if content[0] == "зачистка":
#            if data.message.author.role != 0:
#                for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=10).messageId:
#                    sub_client.delete_message(reason="зачистка", chatId=data.message.chatId, messageId=msgId, asStaff=True)

#        if [x for x in ['.tickle', '.kus', '.slap', '.poke', '.hug', '.cuddle', '.feed', '.kiss', '.pat', 'morn', 'night' ] if (x in content)]:
#            sub_client.delete_message(reason="!чисткачата", chatId=data.message.chatId, messageId=data.message.messageId, asStaff=True)


while True:
    if time.time() >= reloadTime:
        print("Updating socket...")
        try:
            client.socket.close()
            client.socket.start()
        except:pass
        print("Updated!")
        reloadTime += 120

