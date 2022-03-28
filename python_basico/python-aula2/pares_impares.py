numbers = [1,2,3,4,5,6]
number_p = 0
number_i = 0

for n in numbers:

    if n % 2 == 0:
        number_p = number_p + n

    elif n % 2 != 0:
        number_i = number_i + n

print(f'Soma total dos números pares: {number_p}')
print(f'Soma total dos números ímpares: {number_i}')