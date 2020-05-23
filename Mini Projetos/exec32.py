# leia um ano e mostre s eé BISSEXTO
ano = int(input("ANO: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} não é BISSEXTO".format(ano))
