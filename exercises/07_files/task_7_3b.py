# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""

cfg = "CAM_table.txt"
cams = []
vlan = int(input("Enter VLAN number: "))

with open(cfg, encoding="utf-8") as src:
    for line in src:
        if "." in line:
            cams.append(line.split())

cams.sort(key=lambda x: int(x[0]))

for cam in cams:
    if vlan == int(cam[0]):
        print(f"{cam[0]:10}{cam[1]:20}{cam[3]}")
