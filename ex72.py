num = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
q = ' '
while True:
    escolha = int(input('Escolha um número entre 0 à 20: '))
    if 0 <= escolha <= 20:
        print(f'{escolha} por extenso é {num[escolha]}')
    else:
        print('\033[1;31mNúmero inválido, tente novamente.\033[m')
    q = str(input('Deseja continuar? [S/N}: ')).upper().strip()[0]
    if q == 'S':
        continue
    else:
        break
print('FIM DO PROGRAMA')




