# verificar se a expressao é valida
lista = []
express = input("Expressão: ")
for letras in express:
    lista.append(letras)
abre = lista.count("(")
fecha = lista.count(")")
if abre == fecha:
    print("É valida!")
else:
    print("Não é valida!")
