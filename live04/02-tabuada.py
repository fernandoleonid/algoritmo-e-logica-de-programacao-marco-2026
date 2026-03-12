contador = 1
numero =  int(input('Digite um número para a tabuada: ')) 

while contador <= 10:
    resultado = numero * contador
    print (f'{numero} x {contador} = {resultado}')
    contador += 1