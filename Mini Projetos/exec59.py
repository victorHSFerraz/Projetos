# ler dois valores e mostrar um menu somar multiplicar qual o maior novos numeros e sair do programa
from time import sleep
option = ""
num1 = int(input("Numero: "))
num2 = int(input("Segundo numero: "))
print()
while option != 5:
    print("=" * 20)
    print('[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior numero \n[ 4 ] Novos numeros \n[ 5 ] Sair do programa')
    print("=" * 20)
    print()
    option = int(input("Opção: "))
    print()
    if option == 1:
        print("Soma: {}".format(num1 + num2))
        print()
    elif option == 2:
        print("Multiplicação: {}".format(num1 * num2))
        print()
    elif option == 3:
        lista = [num1, num2]
        print(max(lista))
        print()
    elif option == 4:
        num1 = int(input("Numero: "))
        num2 = int(input("Segundo numero: "))
    elif option == 5:
        print("Finalizando programa... ")
        sleep(1)
        print()
    elif option > 5:
        print("Numero invalido")
