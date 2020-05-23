# programa de multa quando mais de 80km/h 7 reais cada km excedente
kmBase = 80
kmRegistrada = int(input("Velocidade: "))
if kmRegistrada > kmBase:
    print("Infração cometida. Velocidade além da permitida. ")
    print("Velocidade max permitida {}km/h. Velocidade registrada {}km/h".format(kmBase, kmRegistrada))
    print("Multa: R${:.2f}".format((kmRegistrada - kmBase) * 7))
else:
    print("Velocidade permitida.")
