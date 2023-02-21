import math
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float (input('Informe o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {h:.2f}')


