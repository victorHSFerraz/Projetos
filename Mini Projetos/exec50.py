# ler 6 numeros e somar somente os pares
soma = 0
cont = 0
for num in range(1, 7):
    x = int(input("Digite o {}° valor: ".format(num)))
    if x % 2 == 0:
        soma = soma + x
        cont = cont + 1
print()
print("A soma dos {} valores PARES é igual a {}".format(cont, soma))
