#
# Desempacotamento de listas - PYTHON
#

lista = ['Rafael', 'Roger', 'Rayane', 'Roberta', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2, n3, outra_lista[-1], ultimo_da_lista)

