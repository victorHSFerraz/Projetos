# fibonacci
print("\033[1;31mF I B O N A C C I\033[m")
valor1 = 1
valor2 = 1
x = int(input("\nQuantos termos? "))
print("0 -> {} -> {} -> ".format(valor1, valor2), end="")
cont = 0
while cont != (x - 3):
    valor3 = valor1 + valor2
    print(valor3, end=" -> ")
    valor1 = valor2
    valor2 = valor3
    cont = cont + 1
print("FIM")


