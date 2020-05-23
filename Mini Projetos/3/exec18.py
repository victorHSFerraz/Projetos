# Faça um programa que leia um angulo e exiba na tela o valor do sen cos e tan
import math
angulo = float(input("Valor do angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("Angulo: {} \nSEN: {:.2f} COS: {:.2f} TAN: {:.2f}".format(angulo, sen, cos, tan))
