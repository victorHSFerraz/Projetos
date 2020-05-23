# programa while que só aceite M/F
rep = ""
while rep != "M" and rep != "F":
   print("Digite seu sexo: [ M/F ]")
   rep = input("Informe seu sexo: ").upper()
print("Sexo {} registrado com sucesso!".format(rep))
