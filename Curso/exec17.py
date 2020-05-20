# Faça um programa que leia o cateto oposto e adjacente de um triangulo retangulo e faça o calculo da hipotenusa
import math
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
soma = (ca **2) + (co **2)
h = math.sqrt(soma)
print("Hipotenusa: {:.2f} ".format(h))
# ou usar math.hypot()
