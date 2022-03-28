#Gerador de iterators

def contador():
    indice = 0
    while True:
        yield indice #A função yield gralmente guarda o estado de sus variáveis aplicadas.
        indice += 1

gerador = contador()

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))