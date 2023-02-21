frase = str(input('Escreva uma frase: ')).strip().upper().replace(" ", "")
if frase == frase[::-1]:
    print(f'É UM PALINDROMO, O INVERSO DE {frase} É {frase[::-1]}')

else:
    print(f'NÃO É UM PALINDROMO, O INVERSO DE {frase}, É {frase[::-1]}')