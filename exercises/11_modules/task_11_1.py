# -*- coding: utf-8 -*-
"""
Завдання 11.1

Створити функцію convert_mac, яка конвертує mac-адресу з різних форматів в
1a:1b:2c:2d:3e:3f. Функція повинна мати один параметр: mac_address, який очікує
рядок з MAC-адресою в одному з форматів нижче. Функція повинна повертати рядок
з MAC-адресою у форматі 1a:1b:2c:2d:3e:3f.

Повинна підтримуватись конвертація з таких форматів:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a1b-2c2d-3e3f

Функція також повинна перевіряти, що рядок, який було передано функції, містить
правильну MAC-адресу. MAC-адреса вважається правильною, якщо вона:
* кожен символ, крім роздільників ":-.", це символ у діапазоні a-f або 0-9
* крім роздільники, в MAC-адресі має бути 12 символів

Перевірок вище достатньо для цього завдання, тобто не обов'язково перевіряти
формат адреси точніше.

Якщо як аргумент було передано рядок, який не містить правильну MAC-адресу,
згенерувати виняток ValueError (... має бути замінено на передане значення,
приклади нижче): ValueError: '...'

Перевірити роботу функції на різних MAC-адресах у списку mac_list.

Приклад роботи функції:

In [2]: convert_mac("1a1b.2c2d.3e3f")
Out[2]: '1a:1b:2c:2d:3e:3f'

In [3]: convert_mac("1111.2222.3333")
Out[3]: '11:11:22:22:33:33'

In [4]: convert_mac("111122223333")
Out[4]: '11:11:22:22:33:33'

In [5]: convert_mac("1111-2222-3333")
Out[5]: '11:11:22:22:33:33'

In [6]: convert_mac("1111-2222-33")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [6], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33")
...
ValueError: '1111-2222-33' does not appear to be a MAC address


In [7]: convert_mac("1111-2222-33WW")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33WW")
...
ValueError: '1111-2222-33WW' does not appear to be a MAC address

"""

correct_mac_example = [
    "111122223333",
    "1a1b.2c2d.3e3f",
    "1111-2222-3333",
]

wrong_mac_example = ["1a1b.rrrr.3e3f", "1111tttt3333", "1111-2222-33"]

def convert_mac(mac_str):
    allowed_symbols = "abcdef0123456789"
    mac = mac_str.replace(".", "").replace("-", "").replace(":", "")
    if len(mac) == 12 and all(c in allowed_symbols for c in mac):
        mac = [mac[0:2], mac[2:4], mac[4:6], mac[6:8], mac[8:10], mac[10:12]]
    else:
        raise ValueError(f"{mac_str} does not appear to be a MAC address")
    return ":".join(mac)