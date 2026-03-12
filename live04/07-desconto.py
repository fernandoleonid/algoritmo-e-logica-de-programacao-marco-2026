# Desconto de 5% para valores maior ou igual 40

valores = [19.50, 49.00, 100.00, 15.90, 31.49]

for valor in valores:
    if valor >= 40:
        print (valor * 0.95)
    else:
        print (valor)