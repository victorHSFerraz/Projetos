# programa que leia o ano de nasicmento das pessoas e diga quem ja passou da maioridade e as que nao
import datetime
contMenor = 0
contMaior = 0
actualYear = datetime.datetime.now().year
for x in range(1, 8):
    ano = int(input("Ano de nascimento da {}° pessoa: ".format(x)))
    idade = - ano + actualYear
    if idade >= 0:
        print("Idade da {}° pessoa: {} anos".format(x, idade))
    elif idade < 0:
        print("Ano Inválido")
    elif idade < 18:
        contMenor = contMenor + 1
    elif idade >= 18:
        contMaior = contMaior + 1
print("{} pessoas maiores de idade \n{} pessoas menores de idade".format(contMaior, contMenor))


