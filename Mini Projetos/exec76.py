# tupla com itens e seus respectivos preços
itens = ("Banana", 1.99, "Jaca", 2.20, "Uva", 10.50)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f"{itens[pos]:.<30}", end="")
    else:
        print(f"R${itens[pos]:.2f}")