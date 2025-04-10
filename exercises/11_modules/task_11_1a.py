# -*- coding: utf-8 -*-
"""
Завдання 11.1a

Створити функцію convert_mac_list, яка конвертує список MAC-адрес з різних
форматів в 1a:1b:2c:2d:3e:3f.

Конвертація MAC-адрес повинна виконуватися за допомогою функції convert_mac із
завдання 11.1. Не можна копіювати код функції convert_mac.

Функція convert_mac_list повинна мати два параметри:
* mac_list - чекає як аргумент на список з MAC-адресами
* strict – параметр, який контролює, що робити з неправильними MAC-адресами.
  Можливі значення True/False. Значення за замовчуванням False.

Якщо всі MAC-адреси правильні, функція повинна повернути список цих MAC-адрес,
але у форматі 1a:1b:2c:2d:3e:3f. Якщо якісь MAC-адреси неправильні (функція
convert_mac згенерувала виключення ValueError), залежно від параметра strict
треба:
* якщо strict дорівнює True - не перехоплювати виняток ValueError з функції convert_mac
* якщо strict дорівнює False - ігнорувати неправильні MAC-адреси та додати до
  списку лише ті, що пройшли перевірку

Приклад роботи функції:

In [9]: convert_mac_list(["1a1b.2c2d.3e3f", "111122223333", "1111-2222-3333"], strict=False)
Out[9]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33', '11:11:22:22:33:33']

In [10]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "1111-2222-3333"], strict=False)
Out[10]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33']

In [11]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "1111-2222-3333"], strict=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [11], in <cell line: 1>()
----> 1 convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "1111-2222-3333"], strict=True)
...
ValueError: '1111WWWW3333' does not appear to be a MAC address
"""

from task_11_1 import convert_mac


def convert_mac_list(mac_list: list, strict: bool = False) -> list:
    result = []
    for mac in mac_list:
        try:
            result.append(convert_mac(mac))
        except ValueError:
            if strict:
                raise
    return result
