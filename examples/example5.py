def generator(start = 0, end = 10, step = 1):
    number = start
    while number <= end:
        yield number
        number += step

ranger = generator(1, 14, 2)

for value in ranger:
    print(value)