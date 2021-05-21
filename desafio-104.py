#!/usr/bin/python3

'''
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

print('\nDesafio 1:')
x = 6
y = 7

aux = x
x = y
y = aux

print(x, y)


print('\nDesafio 2:')
x, y = y, x
print(x, y)

