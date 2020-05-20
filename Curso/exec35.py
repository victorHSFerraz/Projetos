# crie um programa que leia 3 retas e diga se podem formar um triangulo
x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))
if x < y + z and y < x + z and z < x + y:
    print("\033[1;32mPode formar um triangulo.\033[m")
else:
    print("\033[1;31mNão pode formar um triangulo.\033[m")
