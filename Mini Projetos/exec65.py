# soma de numeros e media maior valor e menor
cont = soma = 0
lista = []
while cont != 10:
    x = int(input("Digite um numero: "))
    lista.append(x)
    soma = soma + x
    y = input("Quer continuar? S/N ").upper()
    cont = cont + 1
    if y == "N":
        break
print("Voce digitou {} numeros. \nA soma entre eles é {}, e a média é {:.2f}".format(cont, soma, soma/cont))
print("O maior numero é {} e o menor {}.".format(max(lista), min(lista)))
