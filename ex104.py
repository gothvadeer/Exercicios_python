# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.


def leia_int():
    """
    leitor de números inteiros
    :return: retorna apenas se o valor digitado é inteiro, senão, mostra uma mensagem de erro.
    """
    while True:
        try:
            n = int(input('Digite um número: '))
            print(f'O número digitado foi: {n}')
            break
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro!\033[m')
    return


leia_int()
help(leia_int)
