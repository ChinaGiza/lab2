def get_number(start = 0, end = 1, step = 1):
    for i in range(start, end, step):
        if i % 2 == 1:
            yield i

count_of_num = 30
to_need = [1, 5]
count = 0

for i in get_number(end = count_of_num):
    if count+1 in to_need:
        print(f"{count+1}-е значение: {i}")
    count += 1
print(f"Последнее значение: {i}")