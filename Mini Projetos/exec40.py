# calcular media
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2)/2
if media >= 7.0:
    print("APROVADO!")
elif 7.0 > media >= 5.0:
    print("RECUPERAÇAO!")
elif media < 5.0:
    print("REPROVADO")