# de valor a 3 retas e diga se pode formar um triangulo e que tipo
x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
z = float(input("Valor de z: "))
if x < y + z and y < x + z and z < x + y:
    print("{}, {} e {} podem formar um triangulo".format(x, y, z), end=" ")
    if x == y == z:
        print("Equilátero.")
    elif x == y != z or x != y == z or z == x != y:
        print("Isóceles.")
    elif x != y != z != x:
        print("Escaleno.")
else:
    print("Os valor de {}, {} e {} não podem formar um triangulo.".format(x, y, z))
