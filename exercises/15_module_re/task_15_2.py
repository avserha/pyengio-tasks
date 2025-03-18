# -*- coding: utf-8 -*-
"""
Завдання 15.2

Створити функцію parse_sh_ip_int_br, яка чекає як аргумент на ім'я файлу, в
якому знаходиться вивід команди show ip int br

Функція повинна обробляти вивід команди show ip int br та повертати такі поля:
* Interface
* IP-Address
* Status
* Protocol

Інформація повинна повертатися у вигляді списку кортежів (приклад вивід):
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'administratively down', 'down'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для отримання такого результату використовуйте регулярні вирази.
Перевірити роботу функції на прикладі файлу sh_ip_int_br.txt та
sh_ip_int_br_2.txt.

Приклад виклик функції
In [12]: parse_sh_ip_int_br("sh_ip_int_br.txt")
Out[12]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

In [13]: parse_sh_ip_int_br("sh_ip_int_br_2.txt")
Out[13]:
[('FastEthernet0/0', '15.0.15.2', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.2', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.2', 'down', 'down'),
 ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
 ('Loopback0', '10.2.2.2', 'up', 'up')]

"""


def parse_sh_ip_int_br(filename: str) -> list:
    result = []
    collumn_pos = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.startswith("Interface"):
                collumn_pos = [line.find("Interface"),
                               line.find("IP-Address"),
                               line.find("OK?"),
                               line.find("Method"),
                               line.find("Status"),
                               line.find("Protocol")]
            if collumn_pos and line.startswith("FastEthernet") or \
               line.startswith("Loopback"):
                intf = line[collumn_pos[0]:collumn_pos[1]].strip()
                ip = line[collumn_pos[1]:collumn_pos[2]].strip()
                status = line[collumn_pos[4]:collumn_pos[5]].strip()
                protocol = line[collumn_pos[5]:].strip()
                result.append((intf, ip, status, protocol))
    return result
