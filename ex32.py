s = float(input('Escreva aqui seu salário: R$ '))
if s <= 1250:
    aumento = (15*s) / 100 #(s + (s * 15 /100) forma com menos linha
    novo = s + aumento
    print(f'Seu salário aumentou 15% e agora você irá receber R$ {novo}')
else:
    aumento2 = (10*s) / 100
    novo2 = s + aumento2
    print(f'Seu salário aumentou 10% e agora você irá receber R$ {novo2}')
