from mathseq import seq
#Minha resolução
fibonacci = seq.fibonacci()
limite = 1
while limite != 0:
    limite = int(input('Quantos termos deseja ver? '))
    fib = [next(fibonacci) for f in range(limite)]
    print('->', fib, '<-')
print(f'\033[1;31mFIM DO PROGRAMA')