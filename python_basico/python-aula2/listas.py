genders = ['Male', 'Female'];

names = [];
names.append('cristiano');
names.append('otavio');
names.append('lucia');
print(names);

names[2] = 'Manuel Bandeira';
print(names);

names.pop(0);

print(names);

numbers = [10, 20, 30, 40, 50];

print(numbers[0:1]);
print(numbers[:1]);
print(numbers[0:2]);
print(numbers[:2])
print(numbers[-1]);
print(numbers[-2]);
print(numbers[-3]);

sexos = ('Masculino', 'Feminino', )

print(f'Item 1: {sexos[0]}');
print(f'Item 2: {sexos[1]}');