# escreva um programa para aprovar emprestimos bancarios. valor da casa salario e prestações. prestac nao deveexceder30%
# do salario
valor = float(input("Valor da casa: "))
salario = float(input("Salario: "))
anos = float(input("Em quantos anos: "))
prestacao = valor/(anos * 12)
print()
print("Valor da Casa: R${:.2f} \nSalario: R${:.2f} \nPrestação: {} anos".format(valor, salario, int(anos)))
print()
print("Prestação: {}x de R${:.2f}".format(int(anos * 12), prestacao))
if prestacao > salario * 30/100:
    print("\033[1;31mEmprestimo REJEITADO. O valor da prestação excede o limite para o seu salario. ")
else:
    print("\033[1;32mEmprestimo APROVADO")

