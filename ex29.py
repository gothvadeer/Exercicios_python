import math
km = int(input('Digite quantos km quer viajar: '))
if km <= 200:
    print(f'Você vai pagar R$ {(km*0.50):.2f}')
else:
    print(f'Você vai pagar R$ {(km*0.45):.2f}')
