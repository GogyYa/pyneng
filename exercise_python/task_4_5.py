# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

#__________________________________________________________________________________

#Answer

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

set1 = set(command1.split()[-1].split(','))  #Создаем множество set1 (из строки выкусываем цифры вланов - выходит список, из списка - делаем множесво set1)
set2 = set(command2.split()[-1].split(','))  #Аналогично со второй строкой

print(sorted(list(set1.intersection(set2)))) # сравниваем множества set1 и set2  с помощью метода intersection, с помощью метода list преобразовываем в список и сортируем по возрастанию
