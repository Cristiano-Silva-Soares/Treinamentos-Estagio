salary_f = 0
salary_m = 0

for n in range(2):

    name = str(input('Entre com o seu nome: '))
    sex = str(input('Entre com o seu sexo - f ou m: '))
    salary = float(input('Entre com o seu salário: '))

    if sex in 'f':
        salary_f = salary_f + salary

    elif sex in 'm':
        salary_m = salary_m + salary


print(f'Soma dos salários das mulheres: {salary_f}')
print(f'Soma dos salários dos homens: {salary_m}')


