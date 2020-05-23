# programa de alistamento militar. mostrar idade ano de alistamento
import datetime
ano = int(input("Ano de nascimento: "))
actualYear = datetime.datetime.now().year
idade = (ano - actualYear) * -1
if idade == 18:
    print("Seu alistamento será esse ano ({}).".format(actualYear))
elif idade < 18:
    print("Ainda falta(m) {} ano(s) para o seu alistamento.".format((idade - 18) * -1))
    print("Seu alistamento será em {}.".format(((idade - 18) * -1) + actualYear))
elif idade > 18:
    print("Seu alistamento já passou ({}).".format(((idade - 18) * -1) + actualYear))
