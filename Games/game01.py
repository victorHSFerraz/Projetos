from time import sleep
listaPersonagem = []
menu = 0
personagem = 0
dormir = ""
print("-" * 26)
print("\033[1;31mS W O R D & D E S T I N Y  \033[m")
print("-" * 26)
input("\nPress Enter to Continue...")
while menu != 1 and 2:
    menu = int(input("\n[ 1 ] - COMEÇAR\n[ 2 ] - SAIR\n\n--> "))
    if menu == 2:
        exit()
print()
nome = input("Name: ")
print()
print("-" * 26)
print("- CRIAÇÃO DE PERSONAGEM -")
print("-" * 26)
while personagem != 1 and 2:
    print("[ 1 ] HUMANO - Os membros dessa espécie têm um cérebro altamente desenvolvido, com inúmeras capacidades "
          "\ncomo o raciocínio abstrato, a linguagem, a introspecção e a resolução de problemas complexos.")
    print(
        "\n[ 2 ] SEP - Orcs are of human shape, and of varying size. They are depicted as ugly and filthy, with a taste"
        "\n\tfor human flesh. They are fanged, bow-legged and long-armed;")
    personagem = int(input("\nESCOLHA 1(HUMANO) ou 2(ORC): "))
listaPersonagem.append(personagem)
print()
print("-" * 40)
print("\n\nHollow Creek", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(0.5)
print(".", end="")
sleep(1)
print(" ano 0")
if personagem == 1:
    print(f"\nVoz desconhecida - Acorde {nome}...")
    while dormir != "S" and dormir != "N":
        dormir = input("Acordar? S/N: ").upper().strip()
    if dormir == "N":
        print("\n\033[1;31mWAKE UP MOTHER FUCKER!\033[m")
        print(f"\n{nome} - damn bro, relax")

