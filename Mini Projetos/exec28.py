# jogo de advinha
from random import randint
from time import sleep
computador = randint(0, 5)
print("<=>" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente advinhar...")
print("<=>" * 20)
user = int(input("Tente advinhar: "))
print("\033[1;31mProcessando...\033[m")
sleep(2)
if user == computador:
    print("Acertou!")
else:
    print("Errou! O número em que pensei foi {}.".format(computador))
