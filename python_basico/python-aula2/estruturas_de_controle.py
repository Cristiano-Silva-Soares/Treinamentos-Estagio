age = int( input('Digite a sua idade: '));

if age >= 18:
    print('Adulto.');
elif age < 18 and age >= 12:
    print('Adolescente.');
else:
    print('Criança.');