#PA primeiro termo e razao
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
cont = 0
pa = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont != total:
        print("{} ->".format(pa), end=" ")
        pa = pa + razao
        cont = cont + 1
    mais = int(input("\nMostrar mais termos? Se sim, quantos? Se não, digite 0. "))
print("Total de termos {}.".format(total))