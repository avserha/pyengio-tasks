# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення 
на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я конфігураційного файлу з якого читаються рядки
2 аргумент ім'я файлу, в який будуть записані рядки

Приклад роботи завдання:
$ python task_7_2b.py config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""

import sys

ignore = ["duplex", "alias", "configuration", "end", "service"]

if len(sys.argv) > 2:
    cfg = sys.argv[1]
    new_cfg = sys.argv[2]
    with open(cfg, encoding="utf-8") as src, \
         open(new_cfg, "w", encoding="utf-8") as dst:
        for line in src:
            if not line.startswith("!"):
                if all(i not in line for i in ignore):
                    dst.write(line)
