# -*- coding: utf-8 -*-
"""
Завдання 15.5

Створити функцію generate_description_from_cdp, яка очікує як аргумент на ім'я
файлу, в якому знаходиться вивід команди show cdp neighbors.

Функція повинна обробляти вивід команди show cdp neighbors та генерувати на
підставі виводу команди опис для інтерфейсів.

Наприклад, якщо у R1 такий вивід команди:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для інтерфейсу Eth 0/0 треба згенерувати такий опис:
description Connected to SW1 port Eth 0/1

Функція повинна повертати словник, в якому ключі - імена інтерфейсів, а
значення - команда, яка задає опис інтерфейсу:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'

Перевірити роботу функції на файлі sh_cdp_n_sw1.txt. Приклад виклику функції

In [17]: generate_description_from_cdp("sh_cdp_n_sw1.txt")
Out[17]:
{'Eth 0/1': 'description Connected to R1 port Eth 0/0',
 'Eth 0/2': 'description Connected to R2 port Eth 0/0',
 'Eth 0/3': 'description Connected to R3 port Eth 0/0',
 'Eth 0/5': 'description Connected to R6 port Eth 0/1'}

"""


def generate_description_from_cdp(filename: str) -> dict:
    result = {}
    collumn_pos = None
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.startswith("Device ID"):
                collumn_pos = [line.find("Device ID"),
                               line.find("Local Intrfce"),
                               line.find("Holdtme"),
                               line.find("Capability"),
                               line.find("Platform"),
                               line.find("Port ID")]
                continue
            if collumn_pos:
                device_id = line[collumn_pos[0]:collumn_pos[1]].strip()
                intf = line[collumn_pos[1]:collumn_pos[2]].strip()
                port_id = line[collumn_pos[5]:].strip()
                result[intf] = "description Connected to " \
                               + device_id + " port " + port_id
    return result
