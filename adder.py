


intro = """

                
                     https://kwork.ru/user/alex_500

                      Разработчик Alex_500 Кворк

                         Запустили Моего Бота!
"""

print(intro)

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import os

os.system('"Telegram Adder.exe"')

api_id =                          #enter here api_id
api_hash = '' #Enter here api_hash id
phone = ''          #enter here phone number with country code
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Привет, спасибо за доверие к нам!/n/nНаши боты с полезными скриптами - https://kwork.ru/user/alex_500')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = []
with open(r"ListGood.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue


os.system('CLS')
print(intro)



print('Выберите группу для добавления участников:')
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input("Введите номер: -1001848283683")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)



os.system('CLS')
print(intro)


mode = int(input("Введите 1, чтобы добавить пользователей и нажмите ентр"))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        continue


    try:

        time.sleep(2)
        os.system('CLS')
        print(intro)
        print("Добавляю - Пропускаю из за настроек пользователя: {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Новый Пользователь Будет Добавлен через 60-90 секунд. Ожидайте...")
        time.sleep(random.randrange(60, 90))
    except PeerFloodError:
        print("Flood Error From Telegram. 'Ошибка Флуда' Продолжу работу через 100 сек...")
        print("Ждём {} сек".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("Настройки Пользователя не позволяют Добавить его. Пропускаю")
        print("Ждите 5 секунд...")
        time.sleep(5)
    except:
        traceback.print_exc()
        os.system('CLS')
        print(intro)
        time.sleep(1)
        print(" Продолжу через 5 секунд...!")
        time.sleep(5)
