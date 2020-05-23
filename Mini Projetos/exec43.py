# imc
peso = float(input("Seu peso em kg: "))
altura = float(input("Sua altura em metros: "))
imc = peso/(altura ** 2)
if imc < 18.5:
    print("IMC = {:.2f}, ABAIXO do peso ideal.".format(imc))
elif imc <= 25:
    print("IMC = {:.2f}, peso IDEAL.".format(imc))
elif imc <= 30:
    print("IMC = {:.2f}, SOBREPESO.".format(imc))
elif imc <= 40:
    print("IMC = {:.2f}, OBESIDADE.".format(imc))
elif imc > 40:
    print("IMC = {:.2f}, OBESIDADE MÓRBIDA.".format(imc))
else:
    print("\033[1;31mDados Invalidos")