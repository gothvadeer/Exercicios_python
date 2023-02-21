count = soma = maior = media = menor = 0
q = 'S'
while q == 'S':
    n = int(input('Digite um número inteiro: '))
    q = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    count += 1
    soma += n
    media = soma / count
    if count == 1:
        maior = menor = n
    else:
        if n < maior:
            menor = n
        if n > menor:
            maior = n
print(f'Foram {count} números lidos, a média entre eles é {media}\no maior valor é {maior} e o menor valor é {menor}')