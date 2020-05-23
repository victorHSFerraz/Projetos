# maior numero menor numero
from time import sleep
lista = []
for x in range(1, 6):
    pesoo = float(input("Peso da {}° pessoa: ".format(x)))
    lista.append(pesoo)
sleep(1)
print("██████", end="")
sleep(1.6)
print("████████████", end="")
sleep(0.7)
print("██")
print("O maior peso é {:.2f}Kg".format(max(lista)))
print("O menor peso é {:.2f}Kg".format(min(lista)))
