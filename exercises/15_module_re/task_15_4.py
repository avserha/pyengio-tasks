# -*- coding: utf-8 -*-
"""
Завдання 15.4

Створити функцію get_ints_without_description, яка очікує як аргумент на ім'я
файлу, в якому знаходиться конфігурація пристрою.

Функція повинна обробляти конфігурацію та повертати список імен інтерфейсів, на
яких немає опису (команди description).

Приклад підсумкового списку:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Приклад інтерфейсу з описом:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0

Інтерфейс без опису:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Перевірити функцію на прикладі файлу config_r1.txt.

Приклад виклику функції
In [15]: get_ints_without_description("config_r1.txt")
Out[15]: ['Loopback0', 'Tunnel0', 'Ethernet0/1', 'Ethernet0/3.100', 'Ethernet1/0']

"""


def get_ints_without_description(filename: str) -> list:
    result = []
    intf, found_descr = None, False
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.startswith("!"):
                continue
            if not line.startswith(" "):
                if intf and not found_descr and intf not in result:
                    result.append(intf)
                if line.startswith("interface"):
                    intf, found_descr = line.split()[-1], False
            if found_descr or line.startswith(" description"):
                found_descr = True
                continue
    return result
