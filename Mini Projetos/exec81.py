# ler varios numeros colocar numa lista dizer quantos numeros tem e mostrar em ordem inversa e dizer se 5 aparece
lista = []
while True:
    x = int(input("Digite um valor: "))
    lista.append(x)
    option = input("Quer continuar? S/N: ").upper()
    if option == "N":
        break
print(f"Quantidade de numeros na lista: {len(lista)}")
lista.sort(reverse=True)
print(f"Ordem inversa da lista: {lista}")
print(f"5 aparece na lista: {5 in lista}")