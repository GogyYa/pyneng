# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#_________________________________________________________________________________________

#Answer

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.replace(']' , '').replace('[', '')  # метор реплэйс меняет квадратные скобки AD на пустоту


#В  строке название протокола в виде аббревеатуры, чтоб вывести именно ОСПФ а не О нужно задать это значение. Проверяем действительно ли это оспф. 

if ospf_route[0] == 'O':
    protocol = 'OSPF'
else:
    protocol = ospf_route[0]

ospf_route=ospf_route.split() #  метод стрип возвращает список из строк

#Создаем шаблон 
template1 = '''
Protocol:              {protocol}
Prefix:                {pref}
AD/Metric:             {AD}
Next-Hop:              {NextHop}
Last update:           {lastUp}
Outbound Interface:    {Intf}
'''


#Подставляем значения со списка в созданнй ранее шаблон
print(template1.format(protocol=protocol, pref=ospf_route[1], AD=ospf_route[2], NextHop=ospf_route[4], lastUp=ospf_route[-2], Intf=ospf_route[-1]))  


