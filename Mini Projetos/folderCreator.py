import os

root = '.'
for num in range(1, 86):
    path = f'{root}\{num}'
    os.makedirs(path)