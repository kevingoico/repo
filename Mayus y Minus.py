#Programa hecho por kevin goicoechea
#09/02/2020
#es un programa que pide un texto y muestra cuantas mayus y minus estan en el mismo
def Cont(Palabra):
  minusculas = 0
  indice = 0
  mayusculas = 0
  while indice < len(Palabra):
    letra = Palabra[indice]
    if letra.isupper() == True:
      mayusculas +=1
    else:
      minusculas +=1
    indice += 1

  print("Total mayusculas:" , mayusculas)
  print("Total minusculas:" , minusculas)

Palabra = input("Pon palabra: ")
Cont(Palabra)