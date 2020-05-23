# fatorial
#versao facil com modulo
#from math import factorial
#x = int(input("Numero: "))
#fatorial = factorial(x)
#print(fatorial)
x = int(input("Numero: "))
c = x
c = c - 1
fat = x * c
print("Fatorial de {}! é: {} x {} x".format(x, x, c), end=" ")
while c != 1:
    c = c - 1
    fat = fat * c
    if c != 1:
        n = print("{} x".format(c), end=" ")
    elif c == 1:
        n = print("{} =".format(c), end=" ")
print(fat)








