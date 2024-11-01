# Пример внутренней функции
def outer_1(out_param1, out_param2):
    def inner_1(in_param1, in_param2):
        return in_param1 + in_param2
    return inner_1(out_param1, out_param2)

print(outer_1(5, 6))

# Пример внутренней функции без замыкания
def outer_2(out_param):
    def inner_2(in_param):
        return f'Результат без замыкания: {in_param}'
    return inner_2(out_param)

print(outer_2('testing'))

# Пример внутренней функции с замыканием
def outer_3(out_param):
    def inner_3():
        return f'Результат с замыканием: {out_param}'
    return inner_3

value = outer_3('testing')
print(value())