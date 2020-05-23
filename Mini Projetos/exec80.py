# entrar 5 numeros em uma lista vazia na ordem
lista = []
lista2 = []
for num in range(0, 5):
    x = int(input("Digite um numero: "))
    lista.append(x)
lista.sort()
print(lista)