#PA primeiro termo e razao
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
cont = 0
pa = primeiro
while cont <= 10:
    print("{} ->".format(pa), end=" ")
    pa = pa + razao
    cont = cont + 1
print("end")