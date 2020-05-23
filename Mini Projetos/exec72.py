# ler um numero de 0 a 20 e mostrar por extenso
numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
while True:
    option = int(input("Digite um numero de 0 a 10: "))
    if option <= 10:
        print(f"O numero que voce digitou foi {numeros[option]}")
    else:
        break