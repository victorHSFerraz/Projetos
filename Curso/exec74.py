from random import randint
lista = []
for num in range(1, 11):
    sorteio = randint(1, 1000)
    lista.append(sorteio)
print(lista)
print(max(lista))
print(min(lista))