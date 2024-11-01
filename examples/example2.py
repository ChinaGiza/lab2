# Пример позиционных аргументов
def parrot(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_parrot = parrot('Kesha', 'Red', 3)
print(my_parrot)

# Пример аргумент - ключевые слова
def dog(name, color, age):
    return {'name': name, 'color': color, 'age': age}

my_dog = dog(age = 5, name = 'Bobik', color = 'Brown')
print(my_dog)

#Пример получения/разбиения аргументов - ключевых слов с помощью символа *
def some_args(*args):
    print('Positional argument tuple:', args)

some_args()
some_args(1, 2, 'args')