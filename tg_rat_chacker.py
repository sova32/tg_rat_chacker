api_id = 12345678
api_hash = 'apihash'
phone = '+380123456789'

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# 11111111111111111111111111111111

chats1 = []
last_date1 = None
chunk_size1 = 10000000
groups1 = []

result = client(GetDialogsRequest(
    offset_date=last_date1,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size1,
    hash=0
))
chats1.extend(result.chats)

for chat1 in chats1:
    try:
        if chat1.megagroup == True:
            groups1.append(chat1)
    except:
        continue

print('Виберіть группу для порівняння: ')
i = 0
for g in groups1:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введіть число: ")
target_group1 = groups1[int(g_index)]

print('Працюю...')
all_participants1 = []
all_participants1 = client.get_participants(target_group1, aggressive=False)

print('Зберігаю у файл "members1.csv"...')
with open("members1.csv", "w", encoding='UTF-8') as f:
    writer1 = csv.writer(f, delimiter=",", lineterminator="\n")
    writer1.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants1:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer1.writerow([username, user.id, user.access_hash, name, target_group1.title, target_group1.id])
print()

# 222222222222222222222222222222222

chats2 = []
last_date2 = None
chunk_size2 = 10000000
groups2 = []

result2 = client(GetDialogsRequest(
    offset_date=last_date2,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size2,
    hash=0
))
chats2.extend(result2.chats)

for chat2 in chats2:
    try:
        if chat2.megagroup == True:
            groups2.append(chat2)
    except:
        continue

print('Виберіть группу з якою порівняти: ')
i = 0
for g in groups2:
    print(str(i) + '- ' + g.title)
    i += 1

g_index2 = input("Введіть число: ")
target_group2 = groups2[int(g_index2)]

print('Працюю...')
all_participants2 = []
all_participants2 = client.get_participants(target_group2, aggressive=False)

print('Зберігаю у файл "members2.csv"...')
with open("members2.csv", "w", encoding='UTF-8') as f:
    writer2 = csv.writer(f, delimiter=",", lineterminator="\n")
    writer2.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants2:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer2.writerow([username, user.id, user.access_hash, name, target_group2.title, target_group2.id])
print()

print('Прорівнюю...')

list1 = []
with open("members1.csv", "r", encoding='UTF-8') as f:
    a = csv.reader(f, delimiter=",", lineterminator="\n")
    for r in a:
        list1.append(r)

list2 = []
with open("members2.csv", "r", encoding='UTF-8') as f:
    b = csv.reader(f, delimiter=",", lineterminator="\n")
    for r in b:
        list2.append(r)

data = []
k=0
for i in list1:
    for j in list2:
        if i[1] in j[1]:
            data.append([str(k), i[3], "@" + i[0], i[1]])
            k += 1


print("Пацюки:")
# # расчёт максимальной длинны колонок
max_columns = []  # список максимальной длинны колонок
for col in zip(*data):
    len_el = []
    [len_el.append(len(el)) for el in col]
    max_columns.append(max(len_el))

# вывод таблицы с колонками максимальной длинны строки каждого столбца
# печать шапки таблицы
columns = ["№", "Ім'я", "user name", "id"]
for n, column in enumerate(columns):
    print(f'{column:{max_columns[n] + 1}}', end='')
print()

# печать разделителя шапки '='
r = f'{"=" * sum(max_columns) + "=" * 5}'
print(r[:-1])

# печать тела таблицы
for el in data:
    for n, col in enumerate(el):
        print(f'{col:{max_columns[n] + 1}}', end='')  # выравнвание по правому краю >
    print()
