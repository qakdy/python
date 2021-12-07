import random
import names
import string
import secrets
# 1 Написать скрипт который в создаст список целых чисел.
print('+++++++++++++++++++++++++++++++++++++++')
l_1 = list(range(1, 71))
print("ex_1 =", l_1)
# 2 Написать скрипт который в создаст список целых чётных чисел.
print('+++++++++++++++++++++++++++++++++++++++')
l_2 = list(range(2, 73, 2))
print("ex_2 =", l_2)
# 3 Написать скрипт который в создаст список целых нечётных чисел.
print('+++++++++++++++++++++++++++++++++++++++')
l_3 = list(range(1, 72, 2))
print("ex_3 =", l_3)
# 4 Написать скрипт который из списка целых чисел выведет чётные числа.
print('+++++++++++++++++++++++++++++++++++++++')


def l_even(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    print('ex_4_even_list = ', even_lst)


l_even(l_1)
# 5 Написать скрипт который из списка целых чисел выведет нечётные числа.
print('+++++++++++++++++++++++++++++++++++++++')


def l_odd(lst):
    odd_lst = []
    for num in lst:
        if num % 2 == 1:
            odd_lst.append(num)
    print('ex_5_odd_list = ', odd_lst)


l_odd(l_1)
# 6 Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
print('+++++++++++++++++++++++++++++++++++++++')


def l_5(lst):
    lst_5 = []
    for num in lst:
        if num % 2 == 0 and num % 5 == 0:
            lst_5.append(num)

    print('ex_6 = ', lst_5)


l_5(l_1)
# 7 Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
print('+++++++++++++++++++++++++++++++++++++++')


def l_5(lst):
    lst_5 = []
    for num in lst:
        if num % 2 == 0 and num % 5 == 0:
            lst_5.append(num)

    print('ex_7 = ', len(lst_5))


l_5(l_1)
# 8 Написать скрипт который в создаст список целых рандомных чисел.
print('+++++++++++++++++++++++++++++++++++++++')
l_1 = []
for i in range(70):
    ll = random.randint(0, 99)
    l_1.append(ll)
print('ex_8 =', l_1)
# 9 Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
print('+++++++++++++++++++++++++++++++++++++++')


def ex_9(list_items):
    l9_1 = []
    l9_2 = []
    count = 0
    for i in list_items:
        count += 1
        if count < 5 and count <= len(list_items):
            l9_2.append(i)
        else:
            l9_2.append(i)
            l9_1.append(l9_2)
            l9_2 = []
            count = 0
    return l9_1


print("ex_9 = ", ex_9(l_1))
# 10 Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка,
# список чётных и список нечётных чисел.
print('+++++++++++++++++++++++++++++++++++++++')


def ex10(lst):
        l10 = []
        l10_1 =[]
        for num in lst:
            if num % 2 == 0:
                l10.append(num)
        for num in lst:
            if num % 2 == 1:
                l10_1.append(num)
        print('ex_10_even = ', l10)
        print('ex_10_odd = ', l10_1)


ex10(l_1)
# 11 Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
print('+++++++++++++++++++++++++++++++++++++++')
stars_5 = []
for i in range(70):
    stars = random.sample(range(1, 50), 5)
    stars_5.append(stars)
print("ex_11 = ", stars_5)
# 12 Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
print('+++++++++++++++++++++++++++++++++++++++')
list_sum = list(map(sum, stars_5))
print("ex_12 = ", list_sum)
# 13 Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100.
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”
print('+++++++++++++++++++++++++++++++++++++++')


def ex13(star):
    the_first_list = []
    the_second_list = []
    for i_iii in star:
        if sum(i_iii) >= 100:
            the_first_list.append(i_iii)
        if sum(i_iii) < 100:
            the_second_list.append(i_iii)

    print("ex13 = ", the_first_list)
    print("ex13 = ", the_second_list)


ex13(stars_5)
# 14 Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок
# вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
def ex14(adge):
    if adge >= 0 and adge <= 19:
        print("Вы постарше!Вам точно больше 20:)")
    if adge >= 20 and adge <= 22:
        salary = 1000
        tenk = 10000/salary
        twentyk = (20000/salary)/12
        thirtyk = (30000/salary)/12
        fiftyk = (50000/salary)/12
        hundredk = (100000/salary)/12
        print("10000$ я смогу отложить в кубышку через", tenk, "месяцев")
        print("20000$ я смогу отложить в кубышку через", twentyk, "лет")
        print("30000$ я смогу отложить в кубышку через", thirtyk, "лет")
        print("50000$ я смогу отложить в кубышку через", fiftyk, "лет")
        print("100000$ я смогу отложить в кубышку через", hundredk, "лет")

    if adge >= 23 and adge <= 26:
        salary = 2000
        tenk = 10000 / salary
        twentyk = (20000 / salary) / 12
        thirtyk = (30000 / salary) / 12
        fiftyk = (50000 / salary) / 12
        hundredk = (100000 / salary) / 12
        print("10000$ я смогу отложить в кубышку через", tenk, "месяцев")
        print("20000$ я смогу отложить в кубышку через", twentyk, "лет")
        print("30000$ я смогу отложить в кубышку через", thirtyk, "лет")
        print("50000$ я смогу отложить в кубышку через", fiftyk, "лет")
        print("100000$ я смогу отложить в кубышку через", hundredk, "лет")
    if adge >= 27 and adge <= 45:
        salary = 3000
        tenk = 10000 / salary
        twentyk = (20000 / salary) / 12
        thirtyk = (30000 / salary) / 12
        fiftyk = (50000 / salary) / 12
        hundredk = (100000 / salary) / 12
        print("10000$ я смогу отложить в кубышку через", tenk, "месяцев")
        print("20000$ я смогу отложить в кубышку через", twentyk, "лет")
        print("30000$ я смогу отложить в кубышку через", thirtyk, "лет")
        print("50000$ я смогу отложить в кубышку через", fiftyk, "лет")
        print("100000$ я смогу отложить в кубышку через", hundredk, "лет")
    if adge >=46 and adge <= 100:
        print('Не такой уж вы и старый, введите свой настоящиий возраст')


ex14(int(input("ВВедите ваш возраст: ")))


# 15 Написать функцию которая получив на вход стартовую ЗП Junior QA
# и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании,
# активностей которые может делать QA. Free implementation of function body logic


def salary_qa(salary, stag):
    soft_skills = 1.20
    auto_tests = 1.50
    english_b_2 = 1.30
    english_c_2 = 1.50
    high_education_economist = 1.35
    high_education_programmist = 1.50
    up_stag = 1.10
    skills = [soft_skills, auto_tests, english_b_2, english_c_2, high_education_economist, high_education_programmist]
    zp_1 = []
    zp_1.append(salary)
    years = 0
    while stag > 0:
        zp = zp_1[-1] * up_stag * secrets.choice(skills)
        stag -= 1
        zp_1.append(zp)
        years += 1
        print("Ваша зарплата после", years, "лет: ", zp)


print(salary_qa(int(input("zp = ")), int(input("stag = "))))


# 16 Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
print('+++++++++++++++++++++++++++++++++++++++')
u_names = []
for i in range(70):
    user_names = names.get_full_name()
    u_names.append(user_names)
print("ex_16 = ", u_names)
# 17 Написать скрипт который сгенерирует список имён файлов.
# К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
print('+++++++++++++++++++++++++++++++++++++++')
filename = ''.join(random.choice(string.ascii_letters) for file in range(7))
ex17 = [("%s " + filename) % y for y in range(1, 10)]
print("ex_17 = ", ex17)
# 18 Написать скрипт который сгенерирует список списков.
# Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.
print('+++++++++++++++++++++++++++++++++++++++')
ex18 = []
for i in range(10):
    zero = [names.get_first_name()]
    ex18.append(zero)
    time_formate = "{Year}-{Month}-{Day}"
    year = [str(x) for x in range(2007, 2022)]
    month_range = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    day_range = [str(i).zfill(2) for i in range(1,28)]
    argz = {"Year": random.choice(year),
            "Month": random.choice(month_range),
            "Day" : random.choice(day_range),
            }
    zero.append(time_formate.format(**argz))
print("ex_18 = ", ex18)
# print(time_formate)
# 19 Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
print('+++++++++++++++++++++++++++++++++++++++')
employees = []
for i in range(10):
    zero = [names.get_first_name()]
    employees.append(zero)

    first = "".join(random.choice(string.ascii_lowercase) for file in range(5, 12))
    login = "Login: " + first
    zero.append(login)

    second = string.ascii_letters + string.digits
    parol = ''.join(random.choice(second) for _ in range(20))
    password = "password: " + parol
    zero.append(password)

    letters = string.ascii_lowercase
    random1 = "".join(random.choice(letters) for tt in range(7))
    gmail = random1 + "@gmail.com"
    email = "email: " + gmail
    zero.append(email)

    time_formate = "{Year}-{Month}-{Day}"
    year = [str(x) for x in range(2007, 2022)]
    month_range = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    day_range = [str(i).zfill(2) for i in range(1, 28)]
    argz = {"Year": random.choice(year),
            "Month": random.choice(month_range),
            "Day": random.choice(day_range),
            }
    zero.append(time_formate.format(**argz))
print("ex_19 = ", employees)
# 20 Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),
print('+++++++++++++++++++++++++++++++++++++++')
family = []
for i in range(10):
    zero = "".join(random.choice(string.ascii_lowercase) for file in range(5, 12))
    login = ["Login: " + zero]
    family.append(login)

    first_female = names.get_first_name(gender="female")
    first_male = names.get_first_name(gender="male")

    randommmm_20 = random.choice([first_male, first_female])
    login.append(randommmm_20)


    t_f = random.choice(["True", "False"])
    login.append(t_f)
print("ex_20 = ", family)
# 21 Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
print('+++++++++++++++++++++++++++++++++++++++')
gender = []
for i in range(10):
    zero = "".join(random.choice(string.ascii_lowercase) for file in range(5, 12))
    login = ["Login: " + zero]
    gender.append(login)


    first = names.get_first_name(gender="female")
    first_1 = names.get_first_name(gender="male")
    randommmm = secrets.choice([first, first_1])
    login.append(randommmm)

    if randommmm == first:
        second = 0
        login.append(second)
    else:
        second = 1
        login.append(second)

print("ex_21 = ", gender)
# 22 Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
print('+++++++++++++++++++++++++++++++++++++++')
salary = []
for i in range(10):
    zero = "".join(random.choice(string.ascii_lowercase) for file in range(5, 12))
    login = ["Login: " + zero]
    salary.append(login)

    first = names.get_first_name()
    login.append(first)

    salary_s = random.randint(300, 5001)
    # ss = str(salary_s) + "$"
    login.append(salary_s)

print("ex_22 =", salary)
# 23 Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$
print('+++++++++++++++++++++++++++++++++++++++')
rich = []
for salary_s in salary:
    if salary_s[2] >= 1500:
        rich.append(salary_s[1])
print("ex_23 = ", rich)


# 24 Написать скрипт который создаст список имён мужчин из gender.
print('+++++++++++++++++++++++++++++++++++++++')
male = []
for second in gender:
    if second[2] == 1:
        male.append(second[1])
print("ex_24 = ", male)
# 25 Написать скрипт который создаст список имён женщин из gender.
print('+++++++++++++++++++++++++++++++++++++++')
female = []
for second in gender:
    if second[2] == 0:
        female.append(second[1])
print("ex_25 = ", female)
# 26 Написать скрипт который создаст список имён неженатых мужчин из family.
print('+++++++++++++++++++++++++++++++++++++++')
unmarried_male = []
for t_f in family:
    if t_f[2] == "False":
        unmarried_male.append(secrets.choice([t_f[1]]))

print("ex_26 = ", unmarried_male)
# 27 Написать скрипт который создаст список имён незамужних женщин из family.
print('+++++++++++++++++++++++++++++++++++++++')
unmarried_female = []
for t_f_1 in family:
    if t_f_1[2] == "False":
        unmarried_female.append(t_f_1[1])

print("ex_27 = ", unmarried_female)
# 28 Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$.
# Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций
print('+++++++++++++++++++++++++++++++++++++++')
# script = []
# for i_1 in family:
#     if i_1[2] == "False":
#         for i_2 in gender:
#             if i_2[2] == 1:
#                 for i_3 in salary:
#                     if i_3[2] >= 1500:
#                         # if i_1[1] == i_2[1] == i_3[1]:
#                         script.append(i_2[1])

# print("ex_28 = ", script)
print('ex_28 = должны быть одинаковые списки везде, но скрипт записан и закомичен')
# 29 Использовать функцию для 28 задания
print('+++++++++++++++++++++++++++++++++++++++')
#
#
# def func(f, num, s_s):
#     function = []
#     for i_1 in family:
#         if i_1[2] == f:
#             for i_2 in gender:
#                 if i_2[2] == int(num):
#                     for i_3 in salary:
#                         if i_3[2] >= int(s_s):
#                             if i_1[1] == i_2[1] == i_3[1]:
#                                 function.append(i_2[1])
#     print("ex_29 = ", function)
#
#
# func("False", 1, 1500)
print('ex_29 = должны быть одинаковые списки везде, но функция записана и закомичена')