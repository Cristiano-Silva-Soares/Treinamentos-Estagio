age = int(input('Digite a sua idade: '))

while age < 18:
    print('Você é menor de idade!')
    age = int(input('Digite a sua idade: '))

if age == 18:
    print("Você é maior de idade!")