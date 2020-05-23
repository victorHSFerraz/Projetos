# ler o nome e preço de varios produtos perguntar se o usuario quer continuar e mostrar o menor e o maior preço e produtos acima de 1000 reais
lista1 = []
cont = 0
total = 0
while True:
    produto = input("Produto: ")
    preco = float(input("Preço: "))
    lista1.append(preco)
    total = total + preco
    if preco >= 1000:
        cont = cont + 1
    option = input("Quer Continuar? S/N: ").upper().strip()
    if option == "S":
        print()
    else:
        break
print(f"\nTotal: R${total:.2f} \nMaior preço R${max(lista1):.2f} \nmenor preço R${min(lista1):.2f}")
print(f"Produtos acima de R$1000.00: {cont}")


