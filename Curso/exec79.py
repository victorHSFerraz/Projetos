# adicionar valores a lista. sem repetir. ordem crescente
lista = []
option = ""
while True:
    valor = int(input("Adicionar valor a lista: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("Erro. Valor Duplicado.")
    option = input("Deseja continuar? S/N: ").upper()
    if option == "N":
        break
lista.sort()
print(lista)
print("FIM")