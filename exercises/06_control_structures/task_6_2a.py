# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = input('Please enter ip address: ')
if ip.count('.'):
    ip_list = ip.split('.')
    a = len(ip_list)
    if a == 4:
        b = 0
        while b <= (a-1):
            if int(ip_list[b]) in range(0, 256):
                b += 1
                continue
            else:
                print("it's not correct ip address")
                break
        else:
            print("it's correct ip address")
            if int(ip_list[0]) >= 1 and int(ip_list[0]) <= 223:
                print("it's unicast")
            elif int(ip_list[0]) >= 224 and int(ip_list[0]) <= 239:
                print("it's multicast")
            elif int(ip_list[0]) == 255:
                i = 1
                while int(ip_list[i]) == 255 and i < 3:
                    i += 1
                    continue
                else:
                    if i == 3:
                        print ("it's local broadcast")
                    else:
                        print("it's unused")
            elif int(ip_list[0]) == 0:
                for n in range(1, 4):
                    if int(ip_list[n]) == 0:
                        continue
                    else:
                        print("it's unused")
                        break
                else:
                    print("it's unassigned")
            else:
                print("it's unused, dude!")
    else:
        print("it's not correct ip address")
else:
    print("it's not corrects ip address")