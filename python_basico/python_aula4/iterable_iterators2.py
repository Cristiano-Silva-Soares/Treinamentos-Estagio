numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

_numbers = iter(filter(lambda number: number % 2 != 0, numbers))

while True:
    try:
        print(next(_numbers))
    except StopIteration:
        break
        

