from math import sin, cos, tan, radians, trunc
a = float(input('Digite um ângulo: '))
s = sin(radians(a))
print(f'O Seno do ângulo {trunc(a)}º é {s:.2f}')
c = cos(radians(a))
print(f'O cosseno do ângulo {trunc(a)}º é {c:.2f}')
t = tan(radians(a))
print(f'O tangente do ângulo {trunc(a)}ª é {t:.2f}')
