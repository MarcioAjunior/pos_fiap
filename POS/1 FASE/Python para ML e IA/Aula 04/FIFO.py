"""
    Fifo com deque do python, FILA
"""
from collections import deque

fila = deque()

fila.append(1)
fila.append(2)
fila.append(3)

print(fila)

primeiro_elemento = fila.popleft()
ultimo_elemento = fila.pop()


print(f'O primeito elemento da fila é {primeiro_elemento}')
print(f'O ultimo elemento da fila é {ultimo_elemento}')

print(fila)