palavras = ('APRENDER', 'ENSINAR', 'TABUA', 'ONÇA', 'PYTHON', 'CARACOL', 'RAQUETE',
            'LOBO', 'DADO', 'SOL', 'TATU', 'JACA', 'MORAL', 'SEXTA', 'MOTOCICLETA')
vogais = 'AEIOU'
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end=' ')
    for vogal in palavra:
        if vogal in vogais:
            print(f'{vogal}', end=' ')
