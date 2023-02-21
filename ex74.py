import random

num = tuple(random.randint(1, 5) for c in range(5))
print(f'Números sorteados foram:\n{num}')
print(f'Maior número: {max(num)}')
print(f'Menor número: {min(num)}')
