import random as rand

rand_array = [rand.randint(0, 200) for i in range(20)]

try:
    X = int(input("Введите цифру от 1 до 9: "))
    if 0 <= X and X <= 9:
        lambda_mod = lambda sub: sub % X == 0
        result = [i for i in rand_array if lambda_mod(i)]
        if len(result) == 0:
            print(f"В списке нет чисел кратным {X}")
        else:
            print("Результат: ",result)
    else:
        print("Ошибка: Введенное значение не является цифрой")
except:
    print("Ошибка: Введенное значение не является цифрой")