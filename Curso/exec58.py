#jogo de advinha
from random import randint
numram = randint(0, 10)
numjo = ""
tentativas = 0
print("Vou pensar em um numero entre 0 e 10. Tente advinhar!")
while numjo != numram:
    numjo = int(input("Seu palpite: "))
    tentativas = tentativas + 1
    if numjo < numram:
        print("Mais.. Tente mais uma vez!")
    elif numjo > numram:
        print("Menos.. Tente mais uma vez!")
print("Acertou! O numero que eu pensei foi {}.".format(numram))
print("Total de tentativas: {}".format(tentativas))