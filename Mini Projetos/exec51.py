# programa que leia o primeiro termo e a razao de uma PA. Mostre os 10 primeiros termos
first = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
for num in range(1, 11):
    print(first, end=" ")
    first = first + razao
