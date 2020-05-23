# ler varios numeros inteiros e somar. 999 para parar e sem somar
print("Digite numeros inteiros para soma-los. [999] para parar")
soma = 0
cont = 0
num = 0
while 1 > 0:
    num = int(input("numero: "))
    if num == 999:
        break
    else:
        soma = soma + num
        cont = cont + 1
print("{} numeros com soma igual a {}".format(cont, soma))
print("FIM")
