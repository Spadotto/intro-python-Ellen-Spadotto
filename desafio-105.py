#!/usr/bin/python3

'''
    DESAFIO!!!
    1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
    2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

print('\nDesafio 1:')
listapares = [i for i in range(1000) if i % 2 == 0]
print(listapares)

print('\nDesafio 2:')
for i in range(99999999999999999999999999):
    if i % 5 == 0 and i != 0:
        print(i)
        break
