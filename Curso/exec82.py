# varias listas par impar e todos
lista = []
listaPar = []
listaImpar = []
while True:
    x = int(input("Digite um numero: "))
    lista.append(x)
    if x % 2 == 0:
        listaPar.append(x)
    elif x % 2 != 0:
        listaImpar.append(x)
    option = input("Quer continuar? S/N: ").upper()
    if option == "N":
        break
print(lista)
print(listaPar)
print(listaImpar)