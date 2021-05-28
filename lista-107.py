#!/usr/bin/python3

import sys
import timeit


professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)

# Tamanho
print(len(professor1))
# Chaves
print(professor1.keys())
# Valores
print(professor1.values())

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

# Primeira disciplina
print(professor2['courses'][0])

# Utilizando construtor
professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
print(professor3)

# adicionando chave e valor em um dict jah existente
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
print(professor3)

##
# tuplas
##

## Tuplas x listas

#  As tuplas sao estruturas semelhantes as listas; porem, as tuplas sao 'menores' e mais rapidas que as listas para se armazenar dados de maneira ordenada.
# Ao contrario das listas, as tuplas sao imutaveis (immutable). Ou seja, uma vez que sao criadas, as tuplas sao estaticas e isso garante uma melhor performance nos casos em que podem ser aplicadas.
# As listas demandam um maior custo, mas permitem adicionar, remover e alterar os seus dados. Ou seja, a lista é mutavel.

# lista
list = [2, 3, 5, 7, 11, 13, 17, 19]
# tupla
tuple = (2, 3, 5, 7, 11, 13, 17, 19)

# mesmo tamanho
print(len(list))
print(len(tuple))

# encerra o script sem saida de erro
# comente ou mude de linha para estudar o resto do arquivo


# iteracao identica
for p in list:
    print(p)

for p in tuple:
    print(p)

# tamanho das tuplas eh bem menor. Pode ser significante ao se trabalhar com grande quantidade de dados
print('Tamanho lista: ', sys.getsizeof(list))
print('Tamanho tupla: ', sys.getsizeof(tuple))

# tamanho de um range (lembram da ultima aula?)
print('Tamanho range: ', sys.getsizeof(range(9)))
print('Tamanho range: ', sys.getsizeof(range(999999999999999999)))

# por ser imutavel, as tuplas sao criadas mais rapidamente
# tempo para cria um milhao de listas e tuplas (aumente essa quantidade, progressivamente, para perceber o efeito)
list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1_000_000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1_000_000)


print('Tempo lista:', list_time)
print('Tempo tupla:', tuple_time)
percent = tuple_time / list_time * 100
print(f'{percent}% mais rapido')


# as tuplas nao precisam dos parenteses para serem criadas
t1 = (1, 2)
t2 = 1, 2

print(type(t1))
print(type(t2))
print(t1 == t2)

# Unpack de tupla. Formato (idade, cidade, vacinado)
survey = (22, 'Canoinhas', False)
age, city, vaccined = survey

print(f'idade: {age}; cidade: {city}; vacinado: {vaccined}')

# Acesso por indice
print(survey[2])

# Detalhes
empty_tuple = ()
tuple1 = ('teste1')
tuple2 = ('teste1', 'teste2')

print(type(empty_tuple))
print(type(tuple1))
print(type(tuple2))

# Forcar tuple1 a ser uma tupla

tuple1 = ('teste1', )
print(type(tuple1))

###
# Exercicio
###

print('\n')
print('Resolução dos exercicios: \n')

print('\nQuestao 1:')
# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
list = [1, 2, 3, 4, 5, 6, 7]
tuple = (1, 2, 3, 4, 5, 6, 7)

print("Inserindo no final da Lista:")
list.append(21)
print(list)

print("Concatenando Lista:")
list.extend(list)
print(list)

print("Inserindo em determinada posição:")
list.insert(0, 0)
print(list)

print("Removendo elemento da lista:")
list.remove(0)
print(list)


print("Remove o que está no final da lista:")
list.pop()
print(list)


print("Descobrindo o índice do número 6 na Lista:")
print(list.index(6))

print("Numero de vezes que o 2 aparece na Lista:")
print(list.count(2))

print("Invertendo lista:")
list.reverse()
print(list)

print("Ordenando lista:")
list.sort()
print(list)

print("Tuplas são imutáveis em sua maioria, com poucas exceções.")
print("Tuplas não possuem o atributo append;")
print("Tuplas não possuem o atributo extend;")
print("Tuplas não possuem o atributo insert;")
print("Tuplas não possuem o atributo remove;")
print("Tuplas não possuem o atributo pop;")
print("Tuplas não possuem o atributo reverse;")
print("Tuplas não possuem o atributo sort;")

print("Descobrindo o índice do número 6 na Tupla:")
print(tuple.index(6))

print("Numero de vezes que o 2 aparece na Tupla:")
print(tuple.count(2))

print('\nQuestao 2:')
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
metodoslista = 9
metodostupla = 2
print('\nA diferença de métodos se uma lista para uma tupla é: ', metodoslista - metodostupla)

print('\nQuestao 3:')
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.
professor1['latitude/longitude'] = ('180', '65')
professor2['latitude/longitude'] = ('73', '13')
professor3['latitude/longitude'] = ('99', '82')

print(professor1)
print(professor2)
print(professor3)


