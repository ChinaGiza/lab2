import random as r

items = ["камень", "ножницы", "бумага"]

def stone_scissors_paper(fp_choice, sp_choice, fp_name, sp_name):
    if (fp_choice == sp_choice):
        print(f"Ничья. Так как оба игрока выбрали {fp_choice}")
        return 0, 0
    elif ((fp_choice == "камень" and sp_choice == "ножницы") or
          (fp_choice == "ножницы" and sp_choice == "бумага") or
          (fp_choice == "бумага" and sp_choice == "камень")):
        print(f"{fp_name} побеждает {sp_name}, так как {fp_choice} бьет {sp_choice}")
        return 1, 0
    else:
        print(f"{sp_name} побеждает {fp_name}. Так как {sp_choice} бьет {fp_choice}")
        return 0, 1

def computer_choice():
    global items
    choice = r.randint(0,29)
    return items[choice//10]

def player_choice():
    global items
    while True:
        choice = input(">>> Введите камень, ножницы или бумага: ").lower()
        if choice in items or choice in ["q", "й"]:
            return choice
        else:
            print("!!! Ошибка: Введено некорректное значение")

def score_result(fp_score, sp_score, fp_name, sp_name):
    if fp_score == sp_score:
        print(f"### Ничья. Счет: {fp_score}:{sp_score}")
    elif fp_score > sp_score:
        print(f"### Побеждает {fp_name}. Счет: {fp_score}:{sp_score}")
    else:
        print(f"### Побеждает {sp_name}. Счет: {sp_score}:{fp_score}")

def mode_1():
    fp_score, sp_score = 0, 0
    rounds = input(">>> Введите количество раундов (в пределах от 1 до 100 или \"inf\" для бесконечной игры: ").lower()
    if rounds == "inf" or (rounds.isdigit()):
        print("!!! Внимание: Введите \"q\" или \"й\" для выхода из игры")
        if rounds == "inf":
            print("### Игра начинается!")
            while True:
                fp_choice = player_choice()
                if fp_choice in ["q", "й"]:
                    print("!!! Внимание: Выход из текущей игры")
                    break
                else:
                    fp_subscore, sp_subscore = stone_scissors_paper(fp_choice, computer_choice(), "Игрок", "Бот")
                    fp_score += fp_subscore
                    sp_score += sp_subscore
            score_result(fp_score, sp_score, "Игрок", "Бот")
        else:
            rounds = int(rounds)
            if 0 < rounds < 101:
                print("### Игра начинается!")
                round = 0
                while round < rounds:
                    print(f"### Раунд {round + 1}")
                    fp_choice = player_choice()
                    if fp_choice in ["q", "й"]:
                        print("!!! Внимание: Выход из текущей игры")
                        break
                    else:
                        fp_subscore, sp_subscore = stone_scissors_paper(fp_choice, computer_choice(), "Игрок", "Бот")
                        fp_score += fp_subscore
                        sp_score += sp_subscore
                        round += 1
                if round == rounds:
                    score_result(fp_score, sp_score, "Игрок", "Бот")
                else:
                    print(f"### Счет на момент выхода: Игрок - {fp_score} и Бот - {sp_score}")
            else:
                print("!!! Ошибка: Количество раундов не находится в пределах от 1 до 100")
    else:
        print("!!! Ошибка: Введенно некорректное значение")

def mode_2():
    fp_score, sp_score = 0, 0
    rounds = input(">>> Введите количество раундов (в пределах от 1 до 100): ")
    if rounds.isdigit():
        rounds = int(rounds)
        if 0 < rounds < 101:
            print("### Игра начинается!")
            round = 0
            while round < rounds:
                print(f"### Раунд {round + 1}")
                fp_subscore, sp_subscore = stone_scissors_paper(computer_choice(), computer_choice(), "Бот 1", "Бот 2")
                fp_score += fp_subscore
                sp_score += sp_subscore
                round += 1
            score_result(fp_score, sp_score, "Бот 1", "Бот 2")
        else:
            print("!!! Ошибка: Количество раундов не находится в пределах от 1 до 100")
    else:
        print("!!! Ошибка: введенное значение не является натуральным числом")

def game():
    print("Добро пожаловать в игру Камень-Ножницы-Бумага")
    while True:
        mode = input(">>> Выберите режим:\n* 1 - игрок против компьютера\n* 2 - компьютер против компьютера\n* q или й - выход из программы\n>>> Поле ввода (номер режима): ").lower()
        if mode == "1":
            mode_1()
        elif mode == "2":
            mode_2()
        elif mode in ["й", "q"]:
            print("!!! Выход из программы...")
            break
        else:
            print(">>> Ошибка: был введен не номер режима")

if __name__=="__main__":
    game()