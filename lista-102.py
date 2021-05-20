#!/usr/bin/python3

# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [inicio:fim:passo]

weekdays = ['mon','tues','wed','thurs','fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

print(test)

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

print(all_days)

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))

print('\n')
print('Resolução dos exercicios: \n')

# list.reverse()
# print(list)

#########
# Exercicios - Listas
# Faca sem usar loops
#########

print('Questao 1:')
# Como selecionar 'wed' pelo indice?
day = all_days[2]
print(day)
print(all_days[2])
print(all_days[-5])

print('\nQuestao 2:')
# Como verificar o tipo de 'mon'?
print(type(all_days[0]))

print('\nQuestao 3:')
# Como separar 'wed' até 'fri'?
print(weekdays[2:])
print(all_days[2:5])

print('\nQuestao 4:')
# Quais as maneiras de selecionar 'fri' por indice?
day = all_days[4]
print(day)
print(all_days[4])
print(all_days[-3])

print('\nQuestao 5:')
# Qual eh o tamanho dos dias e days_list?
print('Tamanho de days_list:', len(days_list))
print('Monday', len(days_list[0]))
print('Tuesday', len(days_list[1]))
print('Wednesday', len(days_list[2]))
print('Thursdays', len(days_list[3]))
print('Friday', len(days_list[4]))
print('Saturday', len(days_list[5]))
print('Sunday', len(days_list[6]))

print('\nQuestao 6:')
# Como inverter a ordem dos dias?
print(all_days[::-1])
all_days.reverse()
print(all_days)

print('\nQuestao 7:')
# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')
print(list)
list2 = list[::]

print('\nQuestao 8:')
# Como limpar list?
list.clear()
print(list)

print('\nQuestao 9:')
# Como deletar list?
del list
print('Lista deletada!')

print('\nQuestao 10:')
# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
list = list2[::]
del list2
ultimo_elemento = list[-1]
list.remove(ultimo_elemento)
print(list)

