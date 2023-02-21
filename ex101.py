#Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(x=0):
    from datetime import date
    data = date.today().year
    if nasc == 0 or nasc <= 1900:
        return f'IDADE INVÁLIDA! uma pessoa com {data-nasc} não está viva!'
    elif data-nasc < 18:
       return f'Com {data-nasc} anos: NÃO VOTA!'
    elif 18 >= data-nasc < 65:
        return f'Com {data-nasc} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {data-nasc} anos: VOTO FACULTATIVO!'

#programa principal
while True:
    try:
        nasc = int(input('Ano de nascimento: '))
        print(voto(nasc))
        break
    except ValueError:
        print('ERRO! Digite um número inteiro')



