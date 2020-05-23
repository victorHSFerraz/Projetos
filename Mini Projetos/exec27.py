# programa q mostre primeiro e ultimo nome de uma pessoa
name = input("Nome: ").title().strip()
name = name.split()
print("Primeiro: {}".format(name[0]))
print("Ultimo: {}".format(name[-1]))
