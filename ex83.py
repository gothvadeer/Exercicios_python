expressao = str(input('Digite sua expressão: '))
lista = []
for i in expressao:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Parabéns, sua expressão é válida!')
else:
    print('Infelizmente sua expressão está errada!')