# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_input = input('Введите IP адрес: ')


if ip_input.count('.') == 3:
    a = 1
else:
    print('Неправильный IP-адрес')
    exit()

ip = ip_input.split('.')

for i in ip:
    if i.isdigit() == False:
        print('Неправильный IP-адрес')
        exit()
    else:

        if len(ip) != 4:
            print('Неправильный IP-адрес')
            exit()

for octet_ip in ip:
     if int(octet_ip) > 255:
        print('Неправильный IP-адрес')
        exit()




if int(ip[0]) < 224 and ip_input != "0.0.0.0":
    print('unicast')
elif int(ip[0]) > 223 and int(ip[0]) < 240:
    print('multicast')
elif ip_input == "255.255.255.255":
    print('local broadcast')
elif ip_input == "0.0.0.0":
    print('unassigned')
else:
    print('unused')
