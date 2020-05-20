# ler uma frase e dizer se é um palindromo
frase = str(input("Frase: ")).strip().lower()
frase = frase.replace(" ", "")
print("O inverso de {} é {}".format(frase, frase[::-1]))
if frase == frase[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")