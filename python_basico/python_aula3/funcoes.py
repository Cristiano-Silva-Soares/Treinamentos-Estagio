def somar(a, b):
    return a + b

def subtrair (a:int, b:int):
    return a - b

def multiplicar(a: int, b: int) -> float:
    return a * b

print(somar(20, 20))
print(subtrair(20, 20))
print(multiplicar(b = 10, a = 20))

print_message= lambda a, b: a + b

print(print_message(1,2))