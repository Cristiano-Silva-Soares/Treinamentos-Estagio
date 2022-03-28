name: str = "Cristiano Silva";
age: int = 22;
salary: float = 1000;
married: bool = False;

print(f'Nome: {name}');
print(f'Idade: {age}');
print(f'Salario: {salary}');
print(f'Casado: {married}');

result = salary >= 1000;

print(result)

result = not age == 35 and 'O' in name;

print(result);
