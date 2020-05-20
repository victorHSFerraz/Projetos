# preço produto forma de pagamento a vista 10% desconto cartao a vista 5% desc e em 3x ou mais 20% de juros
preço = float(input("Informe o preço do produto: R$"))
print("Formas de Pagamento:1 - Dinheiro \n\t\t\t\t\t2 - Cartão")
selec = int(input("Forma de Pagamento: "))
if selec == 1:
    print("10% de desconto em pagamento à vista.")
    print("Preço com desconto aplicado: R${:.2f}".format(((preço * 0.1) - preço) * -1))
elif selec == 2:
    print("1 - 5% de desconto em pagamento à vista.")
    print("2 - Preço inalterado em 2x.")
    print("3 - 20% de JUROS em 3x ou mais.")
    cartao = int(input("Parcelamento em quantas vezes: "))
    if cartao == 1:
        print("Total: R${:.2f}".format((preço * 0.05) - preço))
    elif cartao == 2:
        print("2x R${:.2f} TOTAL R${:.2f}".format(preço / 2, preço))
    elif cartao == 3:
        tresVezes = (preço * 0.2) + preço
        print("3x R${:.2f} \nTOTAL R${:.2f}".format(tresVezes/3, tresVezes))
    elif 4 <= cartao <= 12\
            :
        tresVezes = (preço * 0.2) + preço
        print("{}x R${:.2f} \nTOTAL R${:.2f}".format(cartao, tresVezes/cartao, tresVezes))
    else:
        print("ERROR")

