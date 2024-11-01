import datetime as dt

def age():
    while True:
        raw_data = [int(i) for i in input("Введите свой день рождения в формате \"день/месяц/год\": ").split("/")]
        if len(raw_data) != 3:
            print("Ошибка: Введено некорректное значение")
            continue
        try:
            birthday_parsed = [int(i) for i in raw_data]
            try:
                birthday = dt.date(birthday_parsed[2], birthday_parsed[1], birthday_parsed[0])
                today_date = dt.date.today()
                age = today_date.year - birthday.year - ((today_date.month, today_date.day) < (birthday.month, birthday.day))
                print(f"Ваш возраст {age}")
                break
            except:
                print("Ошибка: Введено некорректное значение")
                continue
        except:
            print("Ошибка: Введено некорректное значение")
            continue
        
if __name__=="__main__":
    age()