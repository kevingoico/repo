#Programa hecho por kevin goicoechea
#09/02/2020
#Es un programa que pide 3 numeros y te devuelve el más grande.
def grande (num1,num2,num3):
    true = num1
    if true<num2:
        true = num2
    if true<num3:
        true = num3
    print('este es el numero más grande', true)

num1=int(input('pon el primer numero: '))
num2=int(input('pon el segundo numero: '))
num3=int(input('pon el ultimo numero: '))
print('estos son los numeros: ',num1,num2,num3)
grande(num1,num2,num3)