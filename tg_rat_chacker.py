api_id = 12345678
api_hash = 'api_hash'
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

print('Виберіть группу для порівняння: ')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введіть число: ")
target_group = groups[int(g_index)]

print('Працюю...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=False)

print('Зберігаю у файл "members1.csv"...')
with open("members1.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
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
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
print()

# 222222222222222222222222222222222

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

print('Виберіть группу з якою порівняти: ')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введіть число: ")
target_group = groups[int(g_index)]

print('Працюю...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=False)

print('Зберігаю у файл "members2.csv"...')
with open("members2.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
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
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
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

k = 0
data = []
for l1 in list1[1]:
    k += 1
    for l2 in list2[1]:
        if l1 == l2:
            data.append([str(k), list1[k][3], "@"+list1[k][0], list1[k][1]])

print("Пацюки:")

# расчёт максимальной длинны колонок
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
