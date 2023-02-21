#Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(x=1, show=False):
    """
    O programa faz o calculo do valor dado pelo usuário lido por input.
    :param x: sendo x o valor do input, que tem como padrão 1.
    :param show: se True, mostra como o calculo é feito, se False, mostra apenas o resultado.
    :return: retorna o valor do calculo
    """
    f = 1
    if show:
        for c in range(x, 0, -1):
            f *= c
            print(f' {c} x', end='')
        print(f' = ', end='')
        return f
    else:
        for c in range(x, 0, -1):
            f *= c
        return f'O fatorial de {x} é {f}'


# programa principal

num = int(input('Digite um número: '))
while True:
    explicado = str(input('Quer ver em detalhes?[S/N]: ')).strip().upper()[0]
    if explicado not in 'SN':
        print('OPÇÃO INVÁLIDA! Digite "S" para sim "N" para não.')
    elif explicado == 'S':
        print(fatorial(num, True))
        help(fatorial)
    else:
        print(fatorial(num, False))
    break

