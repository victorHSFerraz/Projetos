# faça um jogo de jokenpo
from random import randint
from time import sleep
print("<->" * 21)
print("\033[7;36;40m J O K E N P Ô \033[m")
print("<->" * 21)
input("PRESS ENTER TO START...")
print()
print("[ 1 ] PEDRA \n[ 2 ] PAPEL \n[ 3 ] TESOURA")
itens = ["Pedra", "Papel", "Tesoura"]
print()
jogador = int(input("ESCOLHA: "))
jogador = jogador - 1
maquina = randint(0, 2)
print()
print("JO", end=" ")
sleep(1)
print("KEN", end=" ")
sleep(1)
print("PÔ")
sleep(1)
print()
print("<->" * 21)
print("O JOGADOR escolheu {}".format(itens[jogador]))
print("A MAQUINA escolheu {}".format(itens[maquina]))
print("<->" * 21)
print()
if maquina == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("\033[1;32m Vencedor: JOGADOR \033[m")
    elif jogador == 2:
        print("\033[1;31m Vencedor: MAQUINA \033[m")
elif maquina == 1:
    if jogador == 0:
        print("\033[1;31m Vencedor: MAQUINA \033[m")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("\033[1;32m Vencedor: JOGADOR \033[m")
elif maquina == 2:
    if jogador == 0:
        print("\033[1;32m Vencedor: JOGADOR \033[m")
    elif jogador == 1:
        print("\033[1;31m Vencedor: MAQUINA \033[m")
    elif jogador == 2:
        print("EMPATE")
