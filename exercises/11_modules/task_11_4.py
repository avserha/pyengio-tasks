# -*- coding: utf-8 -*-
"""
Завдання 11.4

Створити функцію create_network_map, яка обробляє вивід команди show cdp
neighbors з кількох файлів та об'єднує їх у одну загальну топологію.

У функції повинен бути один параметр filenames, який очікує як аргумент на
список з іменами файлів, в яких знаходиться вивід команди show cdp neighbors.

Функція повинна повертати словник, який описує з'єднання між пристроями.
Структура словника така сама, як у завданні 11.3:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Cгенерувати топологію, яка відповідає висновку з файлів:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Не копіюйте код функції parse_cdp_neighbors. Якщо функція parse_cdp_neighbors
не може обробити вивід одного з файлів із виводом команди, треба виправити код
функції у завданні 11.3.

Приклад роботи функції
In [3]: pprint(create_network_map(infiles), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [4]: pprint(create_network_map(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt"]), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

"""

from task_11_3 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


def create_network_map(filenames: list) -> dict:
    result = {}
    for file in filenames:
        with open(file, encoding="utf-8") as f:
            data = parse_cdp_neighbors(f.read())
            result = {**result, **data}
    return result
