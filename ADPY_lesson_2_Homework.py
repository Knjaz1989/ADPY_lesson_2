from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\W?(\d{3})\-?(\d{2})\-?(\d+)\s*\(?([а-яА-я]+[.])?\s*(\d+)?\)?'
repl = r'+7(\2)\3-\4-\5 \6\7'
headers = contacts_list[0]
contacts_list = contacts_list[1:]
new_contacts_list = []
for contact in contacts_list:
    new_contact = []
    for index_item in range(3):
        if contact[index_item]:
            new_contact += contact[index_item].split(' ')
    new_contact.extend([''] * (3 - len(new_contact)))
    new_contact += contact[3:]
    surname, name = new_contact[0], new_contact[1]
    for index_item in range(len(new_contacts_list)):
        item = new_contacts_list[index_item]
        if name in item and surname in item:
            for ind in range(len(new_contacts_list[index_item])):
                if not new_contacts_list[index_item][ind] and new_contact[ind]:
                    new_contacts_list[index_item][ind] = new_contact[ind]
                    new_contact[5] = re.sub(pattern, repl, new_contact[5])
            new_contacts_list[index_item] = new_contact
            break
    else:
        new_contact[5] = re.sub(pattern, repl, new_contact[5])
        new_contacts_list.append(new_contact)
new_contacts_list = [headers] + new_contacts_list


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)
