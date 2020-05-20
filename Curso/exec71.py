# simular caixa eletronico cedulas 50 20 10 1
while True:
    quantia = float(input("Quanto quer sacar? "))
    quant50 = quantia // 50
    resto50 = quantia % 50
    print(f"\n{int(quant50)} cédulas de R$50")
    # print(resto50)
    quant20 = resto50 // 20
    resto20 = resto50 % 20
    print(f"{int(quant20)} cédulas de R$20")
    # print(resto20)
    quant10 = resto20 // 10
    resto10 = resto20 % 10
    print(f"{int(quant10)} cédulas de R$10")
    # print(resto10)
    quant1 = resto10 // 1
    print(f"{int(quant1)} cédulas de R$1")
    option = input("\nDeseja SAIR? S/N ").upper().strip()
    if option == "S":
        break
print("\nFim da operação")