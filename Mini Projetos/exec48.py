# soma de todos os numeros impares entre 1 a 500 multiplos de 3
soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print("A soma dos {} valores é igual a {}".format(cont, soma))
