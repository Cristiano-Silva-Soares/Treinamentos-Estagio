employees = [
    {'name': 'Cristiano', 'gender': 'M', 'salary': 300},
    {'name': 'Maria', 'gender': 'F', 'salary': 1000},
    {'name': 'Lucas', 'gender': 'M', 'salary': 600}
]

# def only_employees(item : dict):
#     return item.get('gender') == 'M'

# print(list(filter(lambda item: item.get('gender') == 'M', employees)))

male = filter(lambda item: item.get('gender') == 'M', employees)
salary = map(lambda item: item['salary'], male)
print(sum(salary))