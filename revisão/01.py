# Calcule e apresente o valor do volume de 
# uma lata de óleo, utilizando a fórmula: 
# volume = π * raio ** 2 * altura. 
# Considere o valor de π como 3.1415.

raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite o altura da lata: "))
PI = 3.1415

volume = PI * raio ** 2 * altura

print (f"O volume da lata de óleo é: {volume}")