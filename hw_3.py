# 1.Создать переменную int_item со значением 10
int_item = 10
# 2. Создать переменную comp_item со значением 18
comp_item = 18
# 3. Создать переменную mult_int в которй умножите int_item на 2
mult_int = int_item * 2
# 4. Создать переменную item_2 со значением True
item_2 = True
# 5. Создать переменную item_3 со значением False
item_3 = False
# 6. Создать переменную item_4 со значением 0
item_4 = 0
# 7. Создать переменную item_5 со значением 1
item_5 = 1
# 8. Создать переменную usd_item со значением ‘usd’
usd_item = 'usd'
# 9. Создать переменную usd_usd_rate со значением 1
usd_usd_rate = 1
# 10. Создать переменную eur_item со значением ‘eur’
eur_item = 'eur'
# 11. Создать переменную usd_eur_rate со значением 0.86
usd_eur_rate = 0.86
# 12. Создать переменную uah_item со значением ‘uah’
uah_item = 'uah'
# 13. Создать переменную usd_uah_rate со значением 26.23
usd_uah_rate = 26.23
# 14. Создать переменную chf_item со значением ‘chf’
chf_item = 'chf'
# 15. Создать переменную usd_chf_rate со значением 0.91
usd_chf_rate = 0.91
# 16. Создать переменную rub_item со значением ‘rub’
rub_item = 'rub'
# 17. Создать переменную usd_rub_rate со значением 71.88
usd_rub_rate = 71.88
# 18. Создать переменную byn_item со значением ‘byn’
byn_item = 'byn'
# 19. Создать переменную usd_byn_rate со значением 2.46
usd_byn_rate = 2.46
# 20. Сделать if в котором будет условие: если mult_int больше comp_item,
# то вывести в консоль (“Переменная mult_int больше”, comp_item)
if mult_int > comp_item:
    print("Переменная mult_int больше", comp_item)
# 21. Создать переменную div_int в которй разделить int_item на 2
div_int = int_item / 2
# 22. Сделать if в котором будет условие: если div_int меньше comp_item,
# то вывести в консоль (“Переменная div_int меньше”, comp_item)
if div_int < comp_item:
    print("Переменная dv_int меньше", comp_item)
# 23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
item_1 = int_item + 10
# 24. Сделать if в котором будет условие: если item_1 меньше comp_item,
# то вывести в консоль (“Переменная item_1 меньше”, comp_item),
# иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)
# 25. Сделать if в котором будет условие: если item_2,
# то вывести в консоль (“Переменная item_2 = ”, item_2),
# иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
if item_2:
    print("Переменная item_2 = ", item_2)
else:
    print("Переменная item_2 = ", item_3)
# 26. Сделать if в котором будет условие: если item_3,
# то вывести в консоль (“Переменная item_3 = ”, item_2),
# иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
if item_3:
    print("Переменная item_3 = ", item_2)
else:
    print("Переменная item_3 = ", item_3)
# 27. Сделать if в котором будет условие: если item_5,
# то вывести в консоль (“Переменная item_5 = ”, item_5),
# иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
if item_5:
    print("Переменная item_5 = ", item_5)
else:
    print("Переменная item_5 = ", item_4)
# 28. Сделать if в котором будет условие: если item_4,
# то вывести в консоль (“Переменная item_4 = ”, item_5),
# иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
if item_4:
    print("Переменная item_4 = ", item_5)
else:
    print("Переменная item_4 = ", item_4)
# 29. Создать переменную currency_convertor со значением item_2
currency_convertor = item_2

# 30. Сделать if в котором будет условие: если currency_convertor,
# то выполнять следующие шаги задания,
# иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
list_v = ["eur", "EUR", "usd", "USD", "uah", "UAH", "chf", "CHF", "byn", "BYN", "rub", "RUB"]
if currency_convertor:
    currency_usd = usd_item
    target_currency = input("Здравствуйте! Выберите валюту,в которую вы хотите перевести доллары: ")
    while target_currency not in list_v:
            print("Неверная валюта, попробуйте еще раз!!!")
            target_currency = input("Здравствуйте! Выберите валюту,в которую вы хотите перевести доллары: ")
            if target_currency in list_v:
                break
    target_currency_amount = float(input("Сколько долларов($) вы хотите перевести?"))
    if target_currency == ('eur'):
        currency_result = target_currency_amount * usd_eur_rate
        print(target_currency_amount, usd_item, "=", currency_result, eur_item)
    elif target_currency == ('EUR'):
        currency_result = target_currency_amount * usd_eur_rate
        print(target_currency_amount, usd_item, "=", currency_result, eur_item)
    elif target_currency == ('uah'):
        currency_result = target_currency_amount * usd_uah_rate
        print(target_currency_amount, usd_item, "=", currency_result, uah_item)
    elif target_currency == ('UAH'):
        currency_result = target_currency_amount * usd_uah_rate
        print(target_currency_amount, usd_item, "=", currency_result, uah_item)
    elif target_currency == ('chf'):
        currency_result = target_currency_amount * usd_chf_rate
        print(target_currency_amount, usd_item, "=", currency_result, chf_item)
    elif target_currency == ('CHF'):
        currency_result = target_currency_amount * usd_chf_rate
        print(target_currency_amount, usd_item, "=", currency_result, chf_item)
    elif target_currency == ('rub'):
        currency_result = target_currency_amount * usd_rub_rate
        print(target_currency_amount, usd_item, "=", currency_result, rub_item)
    elif target_currency == ('RUB'):
        currency_result = target_currency_amount * usd_rub_rate
        print(target_currency_amount, usd_item, "=", currency_result, rub_item)
    elif target_currency == ('byn'):
        currency_result = target_currency_amount * usd_byn_rate
        print(target_currency_amount, usd_item, "=", currency_result, byn_item)
    elif target_currency == ('BYN'):
        currency_result = target_currency_amount * usd_byn_rate
        print(target_currency_amount, usd_item, "=", currency_result, byn_item)
    elif target_currency == ('usd'):
        currency_result = target_currency_amount * usd_usd_rate
        print(target_currency_amount, usd_item, "=", currency_result, usd_item)
    elif target_currency == ('USD'):
        currency_result = target_currency_amount * usd_usd_rate
        print(target_currency_amount, usd_item, "=", currency_result, usd_item)
else:
    print("Переменная currency_convertor = ", item_3)
