intro = """

 ██████╗░███████╗░██████╗████████╗░██████╗
 ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝
 ██████╦╝█████╗░░╚█████╗░░░░██║░░░╚█████╗░
 ██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░░╚═══██╗
 ██████╦╝███████╗██████╔╝░░░██║░░░██████╔╝
 ╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═════╝░

                https://kwork.ru/user/alex_500
                     https://kwork.ru/user/alex_500

               Alex_500 Запустили Нашего Бота!
"""

print(intro)

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
import os

os.system('"Telegram Scrapper.exe"')

api_id = 23842290 #Enter Your 7 Digit Telegram API ID.
api_hash = 'c7892bb3305650803cc005c5f69a2e'   #Enter Yor 32 Character API Hash
phone = '+447466691617 '   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Здравствуйте, это "Alex_500"!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Введите код подтверждения: '))


chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

os.system('CLS')
print(intro)


print('Из какой группы вы хотите спарсить участников:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Пожалуйста! Введите номер: ")
target_group=groups[int(g_index)]

print('Получаю список всех участников...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Список Успешно Сохранен!!!')
with open("ListGood.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow([ 'username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([ username,user.id,user.access_hash,name,target_group.title, target_group.id])
print('Список участников "Успешно" Получен!!! Приступаем...!')
