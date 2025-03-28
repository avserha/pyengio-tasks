# -*- coding: utf-8 -*-
"""
Завдання 9.2

Створити функцію check_ip, яка перевіряє, що рядок, який було передано функції,
містить правильну IP-адресу.

Адреса вважається правильною, якщо вона:
* складається з 4 чисел (а не літер чи інших символів)
* числа розділені точкою
* кожне число в діапазоні від 0 до 255

Функція повинна мати один параметр ip_addr, який очікує рядок з IP-адресою.
Функція повинна повертати True якщо адреса правильна, False інакше.

Перевірити роботу функції на рядках у списку ip_list.
Приклад роботи функції:
In [3]: check_ip("10.1.1.1")
Out[3]: True

In [4]: check_ip("10.500.1.1")
Out[4]: False

In [5]: check_ip("10.a.b.1")
Out[5]: False

In [6]: check_ip("10.1.1.1.")
Out[6]: False

In [7]: check_ip("10.1.1.1.1")
Out[7]: False

In [8]: check_ip("10.1.1.")
Out[8]: False

In [9]: check_ip("10.1.1")
Out[9]: False

In [10]: for ip in ip_list:
    ...:     print(check_ip(ip))
    ...:
True
False
False
True
False

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""

ip_list = ["10.1.1.1",
           "10.3.a.a",
           "500.1.1.1",
           "150.168.100.1",
           "62.150.240.300"]


def check_ip(ip_str: str) -> bool:
    ip = ip_str.split(".")
    if len(ip) != 4:
        return False
    try:
        ip = list(map(int, ip))
    except ValueError:
        return False
    for i in ip:
        if not 0 <= i <= 255:
            return False
    return True
