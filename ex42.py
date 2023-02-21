print('\033[36m=*' * 30)
print('\033[1;33mCALCULE O PREÇO DO SEU PRODUTO EM VÁRIAS FORMAS DE PAGAMENTO')
print('\033[36m=*' * 30)
preço = float(input('\033[mDigite o preço do seu produto: R$ '))
print('\033[1mDIGITE [1] PARA À VISTA DINHEIRO/CHEQUE')
print('''DIGITE [2] PARA A VISTA NO CARTÃO')
DIGITE [3] PARA 2X (CARTÃO)')
DIGITE [4] PARA 3X OU MAIS (CARTÃO)''')
pagamento = int(input('\033[mDigite uma das opções acima: '))
if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'\033[1;32mCOM 10% DE DESCONTO O NOVO PREÇO DO SEU PRODUTO É: R${desconto:.2f}')
elif pagamento == 2:
    desconto2 = preço - (preço * 5 / 100)
    print(f'\033[1;32mCOM 5% DE DESCONTO A VISTA, O NOVO PREÇO DO SEU PRODUTO É: R$ {desconto2:.2f}')
elif pagamento == 3:
    divisão = preço / 2
    print(f'\033[1;32mO PREÇO CONTINUA O MESMO, R$ {preço} DIVIDIDO EM DUAS PARCELAS DE R$ {divisão:.2f}')
elif pagamento == 4:
    parcelas = int(input('Digite o número de parcelas: '))
    juros = preço + (preço * 20 / 100)
    divisão2 = preço / parcelas
    print(f'\033[1;31mSUA COMPRA SERÁ PARCELADA EM {parcelas}X DE R$ {divisão2:.2f} \n'
          f'O NOVO PREÇO COM O ACRÉSCIMO DE 20% DE JUROS É DE {juros:.2f}')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA')
