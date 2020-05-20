# transformar um numero em binario hexa e octa
x = int(input("Digite um numero: "))
print("1 - Binario \n2 - HEXADECIMAL \n3 - OCTAL ")
selec = int(input("Escolha um: "))
if selec == 1:
    print("O numero {} em binario é {}".format(x, bin(x)))
elif selec == 2:
    print("O numero {} em hexadecimal é {}".format(x, hex(x)))
elif selec == 3:
    print("O numero {} em octal é {}".format(x, oct(x)))

