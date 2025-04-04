# -*- coding: utf-8 -*-
"""
Завдання 15.6

Створити функцію convert_mac, яка конвертує mac-адресу з різних форматів в
1a:1b:2c:2d:3e:3f. Функція повинна мати один параметр: mac_address, який очікує
рядок з MAC-адресою в одному з форматів нижче. Функція повинна повертати рядок
з MAC-адресою у форматі 1a:1b:2c:2d:3e:3f.

Повинна підтримуватись конвертація з таких форматів:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a1b-2c2d-3e3f
* 1a:1b:2c:2d:3e:3f (залишити без змін)

Функція також повинна перевіряти, що рядок, який було передано функції, містить
правильну MAC-адресу. MAC-адреса вважається правильною, якщо вона:
* кожен символ, крім роздільників ":-.", це символ у діапазоні a-f або 0-9
* крім роздільники, в MAC-адресі має бути 12 символів

Якщо як аргумент було передано рядок, який не містить правильну MAC-адресу,
згенерувати виняток ValueError (... має бути замінено на передане значення,
приклади нижче): ValueError: '...'

Перевірити роботу функції на різних MAC-адресах у списку mac_list.

Приклад роботи функції:

In [1]: convert_mac("1a1b.2c2d.3e3f")
Out[1]: '1a:1b:2c:2d:3e:3f'

In [2]: convert_mac("1A1B.2C2D.3E3F")
Out[2]: '1A:1B:2C:2D:3E:3F'

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


def convert_mac(mac_address: str) -> str:
    mac_address = mac_address.replace("-", "")
    mac_address = mac_address.replace(".", "")
    mac_address = mac_address.replace(":", "")
    if len(mac_address) != 12 or \
       not all(i.lower() in "0123456789abcdef" for i in mac_address):
        raise ValueError(
            f"'{mac_address}' does not appear to be a MAC address"
        )
    return ":".join(
        [mac_address[i:i+2] for i in range(0, len(mac_address), 2)]
    )
