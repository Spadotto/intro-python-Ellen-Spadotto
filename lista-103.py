#!/usr/bin/python3

'''
    DESAFIO!!!
    Implemente um algoritmo para inverter a ordem de uma string em sua
    linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

## STRINGS
## https://docs.python.org/3/tutorial/introduction.html#strings

msg = 'Minimal Techno Tripping'
size = len(msg)
print('Tamanho de msg:')
print(size)

## Converter para string
s = str(42)
print(s)

s = 'I like you'
print(s)

## Examine as strings colocando prints
s2 = s[0]  # retorna 'I'

s2 = len(s)  # retorna 10

# Como jah fizemos com as listas
s2 = s[0:7]  # retorna 'I like '

s2 = s[6:]  # retorna ' you'

s2 = s[-1]  # retorna 'u'


## concatenar strings
s3 = 'The meaning of life is'
s4 = '42'
s5 = s3 + ' ' + s4       # retorna 'The meaning of life is 42'
s5 = s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter

s = 'Anything you want it to be'
s.split(' ')        # retorna ['Anything', 'you', 'want', 'it', 'to', 'be']
s.split()           # idem


# Entrada via teclado (caracter de escape -> '\')
print('What\'s your name?')
nome = 'qwe'
sobrenome = 'Abreu'
print('Hi, ' + nome)
print('Hi,', nome)

# Formatacao com o metodo format
msg = 'Hi, {} {}!'.format(sobrenome, nome)
print(msg)
msg = f'Hi, {sobrenome} {nome}!'
print(msg)


## Inverter a string
string = 'Hello, my friend!'
print(string)
string2 = string[::-1]
print(string2)

## Substituir
cheese_str = 'I like cheese'
print(cheese_str)
new_cheese_str = cheese_str.replace('like', 'love')
print(new_cheese_str)

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

###
# Exercicios
###

print('\n')
print('Resolução dos exercicios: \n')

print('\nQuestao 1:')
# 1) Extraia o titulo do livro da string
titulo1 = book1.split(' by ')
titulo2 = book2.split(' by ')
titulo3 = book3.split(' by Nassim ')

print('\nQuestao 2:')
# 2) Salve o titulo de cada livro em uma variável
livro1 = titulo1[0]
livro2 = titulo2[0]
livro3 = titulo3[0]

print('\nQuestao 3:')
# 3) Quantos caracteres cada título tem?
print('Livro 1:', len(livro1), 'caracteres')
print('Livro 2:', len(livro2), 'caracteres')
print('Livro 3:', len(livro3), 'caracteres')

print('\nQuestao 4:')
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
autor1, ano1 = titulo1[1].split(', ')
autor2, ano2 = titulo2[1].split(', ')
autor3, ano3 = titulo3[1].split(', ')
print('{} - {}, {}'.format(livro1, autor1, ano1))
print('{} - {}, {}'.format(livro2, autor2, ano2))
print('{} - {}, {}'.format(livro3, autor3, ano3))

print('\nQuestao 5:')
# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
palindrome_one = 'ovo'.upper()
palindrome_two = 'Natan'.upper()
palindrome_three = 'luz azul'.upper().replace(" ","")
palindrome_four = 'caneta azul'.upper().replace(" ","")

primeira = palindrome_one[::-1]
segunda = palindrome_two[::-1]
terceira = palindrome_three[::-1]
quarta = palindrome_four[::-1]

if primeira[::] == palindrome_one[::]:
    print('A palavra "' + palindrome_one + '" é um palindrome')
else:
    print('A palavra "' + palindrome_one + '" não é um palindrome')

if segunda[::] == palindrome_two[::]:
    print('A palavra "' + palindrome_two + '" é um palindrome')
else:
    print('A palavra "' + palindrome_two + '" não é um palindrome')    

if terceira[::] == palindrome_three[::]:
    print('A palavra "LUZ AZUL" é um palindrome')
else:
    print('A palavra "LUZ AZUL" não é um palindrome')
    
if quarta[::] == palindrome_four[::]:
    print('A palavra "CANETA AZUL" é um palindrome')
else:
    print('A palavra "CANETA AZUL" não é um palindrome')
