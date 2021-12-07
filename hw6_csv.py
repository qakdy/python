import csv
import names
import string
import random
import datetime
# 1.Создать пустой empty.csv файл.
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'hw6.csv'
csv_file_name = file_path + file_name

# 2. Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'digits.csv'
csv_file_name_digits = file_path + file_name
with open(csv_file_name_digits, "w") as cf:
    writer = csv.writer(cf)
    for i in range(0, 150):
        writer.writerow([i])

# 3. Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'names.csv'
csv_file_names = file_path + file_name
with open(csv_file_names, "w") as ff:
    writer = csv.writer(ff)
    for i in range(0, 100):
        a = names.get_full_name()
        writer.writerow([a])
# 4. Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'emails.csv'
csv_file_name_email = file_path + file_name
with open(csv_file_name_email, 'w') as em:
    writer = csv.writer(em)
    mail = '@gmail.com'
    for i in range (100):
        filename = ''.join(random.choice(string.ascii_letters) for file in range(7))
        c = filename + mail
        writer.writerow([c])
# 5.Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк.
# Имя и часть email до @ должны совпадать.
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'nne.csv'
csv_file_name_nne = file_path + file_name
with open(csv_file_name_nne, 'w') as nne:
    writer = csv.writer(nne)
    for i in range(100):
        a = names.get_first_name()
        b = 0 + i
        c = a + "@gmail.com"
        writer.writerow([b, a, c])
# 6.Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number,
# в котором будут 300 строк с числами от 10 до 310
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'digits2.csv'
csv_file_name_digits = file_path + file_name
with open(csv_file_name_digits, 'w') as dg:
    a = []
    columns = ['numbers']
    a.append(columns)
    writer = csv.writer(dg)
    for i in list(range(10, 310)):
        ab = []
        ab.append(i)
        a.append(ab)
    writer.writerows(a)
# 7. Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name,
# в котором будут 400 строк с разными именами
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'names_2.csv'
csv_file_names_2 = file_path + file_name
a = []
columns = ['name']
a.append(columns)
with open(csv_file_names_2, "w") as n_2:
    writer = csv.writer(n_2)
    for i in range(401):
        f_name = names.get_first_name()
        a.append([f_name])
    writer.writerows(a)
# 8. Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email,
# в котором будут 400 строк с разными имейлами что-то@gmail.com
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'emails_2.csv'
csv_file_name_email_2 = file_path + file_name
a = []
columns = ['email']
a.append(columns)
with open(csv_file_name_email_2, 'w') as em_2:
    writer = csv.writer(em_2)
    mail = '@gmail.com'
    for i in range(401):
        filename = ''.join(random.choice(string.ascii_letters) for file in range(7))
        c = filename + mail
        a.append([c])
    writer.writerows(a)
# 9. Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк.
# Имя и часть email до @ должны совпадать.
file_path = '/Users/kdy/PycharmProjects/hw6_csv/'
file_name = 'nne_2.csv'
csv_file_name_nne_2 = file_path + file_name
a = []
columns = ['Nubmer', 'Name', 'Email']
a.append(columns)
with open(csv_file_name_nne_2, 'w') as nne_2:
    writer = csv.writer(nne_2)
    for i in range(451):
        first_name = names.get_first_name()
        b = 0 + i
        c = first_name + "@gmail.com"
        a.append([b,first_name,c])
    writer.writerows(a)
