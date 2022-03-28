def sum_numbers(numbers: list):
    pass


def sum_numbers2(*numbers):
    _sum = 0

    for n in numbers:
        _sum += n

    return _sum

sum_numbers([1, 2, 3, 4, 5])
print(sum_numbers2(1, 2, 3, 4, 5, 6))
