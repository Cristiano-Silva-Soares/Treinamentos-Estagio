word = ['p','a','l','a','v','r','a']
vowels = ['a','e','i','o','u']
count_w = 0
count_v = 0

for n in word:

    if n in vowels:
        count_v = count_v + 1

    elif n in word:
        count_w = count_w + 1

print(f'Número de vogais presentes na palavra: {count_v}')
print(f'Número de consoantes presentes na palavra: {count_w}')