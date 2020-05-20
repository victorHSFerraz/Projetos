# ler um numero e dizer se é primo
num = int(input("Numero: "))
cont = 0
print()
for x in range(1, num+1):
    if num % x == 0:
        print("\033[1;32m{}\033[m".format(x), end="  ")
        cont = cont + 1
    else:
        print("\033[1;31m{}".format(x), end="  ")
print("\n\nO numero {} foi divisivel {} vezes.".format(num, cont))
if cont == 2:
    print()
    print("Logo {} é PRIMO.".format(num))
else:
    print()
    print("Logo {} NÃO é primo.".format(num))
