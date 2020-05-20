# lista maior numero e menor e suas posições
lista = []
for num in range(0, 5):
    x = int(input(f"Numero posição {num}: "))
    lista.append(x)
print(f"Maior numero {max(lista)} na posição {lista.index(max(lista))}")
print(f"Menor numero {min(lista)} na posição {lista.index(min(lista))}")

