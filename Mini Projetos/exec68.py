# par ou impar
from random import randint
v = 0
while True:
    jogador = int(input("\nDigite um numero: "))
    escolha = input("Par ou Impar? [ P ] ou [ I ] ").upper().strip()
    computador = randint(1, 10000)
    soma = jogador + computador
    if escolha == "P":
        if soma % 2 == 0:
            print("\nA soma deu: {}".format(soma))
            print("\nVOCE VENCEU!")
            v = v + 1
        else:
            print("\nA soma deu: {}".format(soma))
            print("\nVOCE PERDEU!")
            break
    elif escolha == "I":
        if soma % 2 == 0:
            print("\nA soma deu: {}".format(soma))
            print("\nVOCE PERDEU!")
            break
        elif escolha == "I" and soma % 2 != 0:
            print("\nA soma deu: {}".format(soma))
            print("\nVOCE VENCEU!")
            v = v + 1
print(f"\nVoce venceu {v} vezes.")
