# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#________________________________________________________________________________________________
#
#Answer

file_ospf =  open('/home/git/GogyYa/exercise_python/exercises/07_files/ospf.txt')

template1 = '''
Protocol:              {protocol}
Prefix:                {pref}
AD/Metric:             {AD}
Next-Hop:              {NextHop}
Last update:           {lastUp}
Outbound Interface:    {Intf}
'''
while True:

    line = file_ospf.readline().replace(']' , '').replace('[', '').split()
    #line = line.replace(']' , '').replace('[', '').split()
    #print(line.rstrip())
    if not line:
        break


    if line[0] == 'O':
        protocol = 'OSPF'
    else:
        protocol = line[0]
    print(template1.format(protocol=protocol, pref=line[1], AD=line[2], NextHop=line[4],
                           lastUp=line[-2], Intf=line[-1]))



