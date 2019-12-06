# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#Answer
import sys

network_mask = sys.argv[1]


ip = network_mask
ip_add, mask = ip.split('/')
ip0, ip1, ip2,ip3 = ip_add.split('.') # таким образом сразу назначаются 4 переменных чтоб разбить айпи по октетам.

mask = int(mask) #Меняем тип переменной mask на число - int
count_zero_mask = 32 - mask
mask_b = '1' * mask + '0' * count_zero_mask # Заполняем нулями до 32-х бит маску
net_0 = mask_b[:8] #объевляем 4 октета маски по 8 бит
net_1 = mask_b[8:16]#объевляем 4 октета маски по 8 бит
net_2 = mask_b[16:24]#объевляем 4 октета маски по 8 бит
net_3 = mask_b[24:32]#объевляем 4 октета маски по 8 бит
mask_list = [] #Создаем пустой список, куда поместим 4 октета маски для удобства обращения в дальнейщем - пример:  mask_list[0]
mask_list.append(net_0) #добавляем октеты маски
mask_list.append(net_1)
mask_list.append(net_2)
mask_list.append(net_3)
mask0, mask1, mask2, mask3 = mask_list[0], mask_list[1], mask_list[2], mask_list[3] #Объявляем переменные октетов маски

ip_b = '''{0:08b}{1:08b}{2:08b}{3:08b}'''.format(int(ip0), int(ip1), int(ip2), int(ip3))  # конвертируем заданный в начале айпи в двоичную систему



network_bit = 32 - int(mask) #Определяем кол-во нулей в зависимости от заданной маски
zero_bit = '0' * network_bit
ip_templ = 'ip_b[:-{}]'.format(network_bit)
network = eval(ip_templ) + zero_bit
net_0 = network[:8]
net_1 = network[8:16]
net_2 = network[16:24]
net_3 = network[24:32]
net_list = []
net_list.append(net_0)
net_list.append(net_1)
net_list.append(net_2)
net_list.append(net_3)


#Формируем шаблон
Templ = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{mask}
{mask0:<10}{mask1:<10}{mask2:<10}{mask3:<10}
{mask0:08b}  {mask1:08b}  {mask2:08b}  {mask3:08b}

'''.format(int(net_list[0], 2), int(net_list[1], 2), int(net_list[2],  2), int(net_list[3], 2),mask = mask, mask0 = int(mask0, 2), mask1 = int(mask1, 2), mask2 = int(mask2, 2), mask3 = int(mask3, 2))
print(Templ)
