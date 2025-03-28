# -*- coding: utf-8 -*-
"""
Завдання 11.4a

> Для виконання цього завдання повинен бути встановлений graphviz:
> apt-get install graphviz

> І модуль python для роботи з graphviz:
> pip install graphviz

За допомогою функції create_network_map із завдання 11.4 створити словник топології з описом топології для файлів:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

За допомогою функції draw_topology із файлу draw_network_graph.py намалювати
схему для словника topology, отриманого за допомогою create_network_map. Як
працювати з функцією draw_topology треба розібратися самостійно, почитавши опис
функції файлу draw_network_graph.py. Отримана схема буде записана у svg - його
можна відкрити браузером.

З поточним словником топології на схемі намальовано зайві з'єднання. Вони
виникають тому що в одному файлі CDP (sh_cdp_n_r1.txt) описується з'єднання
("R1", "Eth0/0"): ("SW1", "Eth0/1")
а в іншому (sh_cdp_n_sw1.txt)
("SW1", "Eth0/1"): ("R1", "Eth0/0")

У цьому завданні треба створити нову функцію unique_network_map, яка з цих двох
з'єднань залишатиме лише одне для коректного малювання схеми. При цьому все
одно яке зі з'єднань залишити.

Функція unique_network_map має мати один параметр topology_dict, який очікує як
аргумент словник. Це має бути словник, отриманий у результаті виконання функції
create_network_map із завдання 11.4.

Приклад словника:
{
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
}

Функція повинна повертати словник, який описує з'єднання між пристроями. У
словнику треба позбавитися "дублюючих" з'єднань і залишати тільки одне з них.

Структура підсумкового словника така сама, як у завданні 11.4:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Після створення функції спробувати ще раз намалювати топологію, тепер вже для
словника, який повертає функцію unique_network_map.

Результат має виглядати так само, як схема у файлі task_11_2a_topology.svg

При цьому:
* Розташування пристроїв на схемі може бути іншим
* З'єднання повинні відповідати схемі

Не копіюйте код функцій create_network_map і draw_topology.

Приклад роботи функції
input_topology = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
}

In [7]: pprint(unique_network_map(input_topology))
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

"""

from draw_network_graph import draw_topology
from task_11_4 import create_network_map

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def unique_network_map(topology_dict):
    data = topology_dict
    keys = tuple(data.values())
    for i in keys:
        if i in data.keys() and i in data.values():
            del data[i]
    return data

topology = create_network_map(infiles)
draw_topology(topology)