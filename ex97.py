#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(text):
    tamanho = len(text) + 8
    print('~' * tamanho)
    print(f'{text:^{tamanho}}')
    print('~' * tamanho)


while True:
    texto = str(input('Escreva algo: ')).strip().upper()
    escreva(texto)
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if pergunta in 'SN':
            break
    if pergunta == 'N':
        break
