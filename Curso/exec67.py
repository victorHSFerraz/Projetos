# tabuada de varios numeros. quando negativo encerra
while True:
    tabuada = int(input("Quer a tabuada de qual numero: "))
    if tabuada < 0:
        break
    for num in range(1, 11):
        resultado = num * tabuada
        print(" {} x {} = {}".format(num, tabuada, resultado))
print("\nPrograma Finalizado.")