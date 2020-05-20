# ler varios numeros e somar. 999 para parar
soma = 0
cont = 0
print("Digite numeros para somar (999 para parar)")
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print("A soma dos {} numeros é {}".format(cont, soma))