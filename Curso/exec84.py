lista = []
dados = []
maior = 1.0
menor = 1000.0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    lista.append(dados[:])
    dados.clear()
    option = input("Quer continuar? S/N: ").upper()
    if option == "N":
        break
print(lista)
for peso in lista:
    pesoo = peso[1]
    if pesoo > maior:
        maior = pesoo
    if pesoo < menor:
        menor = pesoo
print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")
