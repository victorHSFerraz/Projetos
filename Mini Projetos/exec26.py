# faça um programa que leie um nome e diga quantos "a" primeira posição e ultima
name = input("Nome: ").lower().strip()
num = name.count("a")
print(num)
print("Primeiro a: {}".format(name.find("a")))
print("Ultimo a: {}".format(name.rfind("a")))
