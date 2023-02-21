produto = float(input('Digite o preço do produto: R$ '))
# como eu fiz:
desconto = (5 * produto) / 100
novop = produto - desconto
# como o professor fez:
# novo = preço - (preço * 5 /100)
#eu que inclui isso
aumento = 10 * produto / 100
novop2 = produto + aumento

print(f'O produto custava R$ {produto:.2f} com 5% de desconto à vista, seu novo preço é de R$ {novop:.2f}')
print(f'Se escolher à prazo, com o aumento de 10% o preço passará de R$ {produto:.2f} para R$ {novop2:.2f}')
