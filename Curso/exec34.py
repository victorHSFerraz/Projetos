# escreva um programa que pergunte o salario c for menor que 1250 tem 15% de aumento, maior q isso 10%
salario = float(input("Salario: "))
if salario < 1250.00:
    aumento = salario * 15/100
    salario = aumento + salario
else:
    aumento = salario * 10/100
    salario = aumento + salario
print("Novo salario: R$ {:.2f}".format(salario))