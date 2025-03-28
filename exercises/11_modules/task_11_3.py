# -*- coding: utf-8 -*-
"""
Завдання 11.3

Створити функцію parse_cdp_neighbors, яка обробляє вивід команди show cdp neighbors.

У функції повинен бути один параметр command_output, який очікує як аргумент на
вивід команди одним рядком (не ім'я файлу). Для цього треба зчитати весь
вміст файлу в рядок, а потім передати рядок як аргумент функції (як передати
вивід команди показано в коді нижче).

Функція повинна повертати словник, який описує з'єднання між пристроями.

Наприклад, якщо як аргумент було передано такий вивід:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функція має повернути такий словник:
{("R4", "Fa0/1"): ("R5", "Fa0/1"),
 ("R4", "Fa0/2"): ("R6", "Fa0/0")}

У словнику інтерфейси мають бути записані без пробілу між типом та ім'ям. Тобто
так Fa0/0, а не так Fa0/0.

Перевірити роботу функції на вміст файлу sh_cdp_n_sw1.txt. При цьому функція
повинна працювати на інших файлах (тест перевіряє роботу функції на файлах
sh_cdp_n_sw1.txt і sh_cdp_n_r3.txt).

Приклад роботи функції
In [3]: with open("sh_cdp_n_sw1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}

In [4]: with open("sh_cdp_n_r1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

In [5]: with open("sh_cdp_n_r2.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

In [6]: with open("sh_cdp_n_r3.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""


def parse_cdp_neighbors(command_output: str) -> dict:
    """
    Тут ми передаємо вивід команди одним рядком, тому що саме в такому вигляді
    буде отримано вивід команди з обладнання. Приймаючи як аргумент вивід
    команди, замість імені файлу, ми робимо функцію більш універсальною: вона
    може працювати з файлами і з виводом з обладнання. Плюс вчимося працювати з
    таким виводом.
    """
    output = command_output.split('\n')
    result = {}
    table_start = False
    local_device = None
    for line in output:
        if "show cdp neighbors" in line:
            local_device = line.split(">")[0]
        if table_start and line != "":
            data = line.strip().split()
            local_device_tuple = (local_device, data[1] + data[2])
            result[local_device_tuple] = (data[0], data[-2] + data[-1])
        if line.startswith("Device ID"):
            table_start = True
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt", encoding="utf-8") as f:
        print(parse_cdp_neighbors(f.read()))
