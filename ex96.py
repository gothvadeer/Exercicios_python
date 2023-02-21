#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(var1, var2):
    print(f'A área do terreno {var1}x{var2} é de {var1 * var2:.1f}m²')


print(f'CONTROLE DE TERRENO'.center(30))
print('-'*30)

largura = float(input('LARGURA m : '))
comprimento = float(input('COMPRIMENTO m: '))
area(largura, comprimento)
