# Пример функции без параметров
def hello_world():
    print("Hello, World!")
# Вызов функции
hello_world()

# Пример возвращающей функции без параметров
def simple_number():
    return 73
# Вызов функции
number = simple_number()
print("Type:", type(number))
print("Result:", number) 

# Пример функции с параметром
def define(number):
    if number < 10:
        return "Number is less than 10"
    elif number == 10:
        return "Number is 10"
    else:
        return "Number is more than 10"

it_is_10 = define(7)
print(it_is_10)