# -*- coding: utf-8 -*-
"""
Завдання 9.6a

Зробити копію функції get_int_vlan_map із завдання 9.6.

Доповнити функцію: додати підтримку конфігурації, коли налаштування порту
access виглядає так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

Тобто, порт знаходиться у VLAN 1

У такому випадку до словника портів повинна додаватися інформація, що порт у
VLAN 1. Приклад словника:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw2.txt
Приклад роботи функції
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


def get_int_vlan_map(config_filename: str) -> tuple:
    access = {}
    trunk = {}
    section = ""
    with open(config_filename, encoding="utf-8") as cfg:
        for line in cfg:
            if line.startswith("!"):
                continue
            if not line.startswith(" "):
                section = line
            if "interface" in section:
                intf = section.split()[-1]
                if "allowed vlan" in line:
                    trunk[intf] = list(map(int, line.strip().split()[-1].split(",")))
                if "access vlan" in line:
                    access[intf] = int(line.strip().split()[-1])
                if "switchport mode access" in line:
                    access[intf] = 1
    return access, trunk
