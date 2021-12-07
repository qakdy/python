# Создать переменную типа string
name = 'Dima'
name_type = type(name)
print(name, name_type)

# Создать переменную типа integer
age = 20
age_type = type(age)
print(age, age_type)

# Создать переменную типа float
temperature = 36.6
temperature_type = type(temperature)
print(temperature, temperature_type)

# Создать переменную типа Bytes
b = bytes(7)
b_type = type(b)
print(b, b_type)

# Создать переменную типа List
array = ['Dima', "The", 'best', 22, False, ]
array_type = type(array)
print(array, array_type)

# Создать переменную типа Tuple
a = tuple('i love QA')
tuple_type = type(a)
print(a, tuple_type)

# Создать переменную типа Set
data = {22, 22, 23, 43}
data.add(14)
set_type = type(data)
print(data, set_type)

# Создать переменную типа Frozenset
new_data = frozenset([23, 3234, 43, 23, True, 'dima', 22])
frozenset_type = type(new_data)
print(new_data, frozenset_type)

# Создать переменную типа Dict
dict_0 = {'password': 19082001,
          'street': 'suharevskaya street',
          'temperature': 36.6,
          'name': 'Dima'}
dict_type = type(dict_0)
print(dict_0, dict_type)

# Создать 2 переменные String, создать переменную в которой сканкентинируе эти переменные
first = 'season'
second = 'work'
end = (first + second)
print(end)

# Вывести в одну строку переменные типа String и Integer используя ","(Запятую)
user_name = 'Dima'
years_old = 20
print(user_name, str(years_old))

# Вывести в одну строку переменные типа String и Integer используя "+"(Плюс)
car = 'BMWX'
model = 5
print(car + str(model))
