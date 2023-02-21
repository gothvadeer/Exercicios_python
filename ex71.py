print('=*' * 20)
print(f"{'BANCO REAL OFICIAL' : ^40}")
print('=*' * 20)
balance = 1500
valoratual = totalced = saquereal = 0
cedulas = [50, 20, 10, 5, 2, 1]
while True:
    print('''ESCOLHA UMA DAS OPÇÕES ABAIXO:
        [ 1 ] SALDO
        [ 2 ] DEPOSITO 
        [ 3 ] EMPRÉSTIMO + SAQUE
        [ 4 ] SAQUE
        [ 5 ] SAIR''')
    escolha = int(input('QUAL A OPÇÃO DESEJA?: '))
    if escolha == 1:
        print(f' Seu saldo é de: {balance}')
    elif escolha == 2:
        deposito = int(input('QUANTO DESEJA DEPOSITAR?: R$ '))
        valoratual = deposito + balance
        print(f'Seu novo saldo é de {valoratual}')
    elif escolha == 3:
        valor = int(input('VALOR DO EMPRÉSTIMO PARA SAQUE: R$ '))
        for cedula in cedulas:
            if valor >= cedula:
                totalced = valor // cedula
                valor = valor % cedula
                if totalced >= 2:
                    print(f'{totalced} cédulas de R$ {cedula},00')
                else:
                    print(f'{totalced} cédula de R$ {cedula},00')
    elif escolha == 4:
        saque = int(input('QUANTO DESEJA SACAR?: R$ '))
        if balance < saque:
            print(f'\033[1;31mSaldo insuficiente! Escolha um valor até {balance}\033[m')
        else:
            saquereal = balance - saque
            print(f'Muito bem, você sacou {saque} de sua conta! Seu novo saldo é de {saquereal} ')
    if escolha == 5:
        print('\033[1mTenha um bom dia!\033[m')
        break
