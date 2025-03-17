# -*- coding: utf-8 -*-
"""
Завдання 9.6

Створити функцію get_int_vlan_map, яка обробляє конфігураційний файл комутатора
та повертає кортеж із двох словників:
* словник портів у режимі access, де ключі номери портів, а значення access
  VLAN (числа)
* словник портів у режимі trunk, де ключі номери портів, а значення список
  дозволених VLAN (список чисел)

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw1.txt

Приклад роботи функції
In [2]: get_int_vlan_map("config_sw1.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [3]: access, trunk = get_int_vlan_map("config_sw1.txt")

In [4]: access
Out[4]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30}

In [5]: trunk
Out[5]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""

def get_int_vlan_map(config_filename):
  access = {}
  trunk = {}
  with open(config_filename) as cfg:
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
  return access, trunk
