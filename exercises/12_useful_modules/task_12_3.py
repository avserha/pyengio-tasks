# -*- coding: utf-8 -*-
"""
Завдання 12.3

Створити функцію print_ip_table, яка відображає таблицю доступних та
недоступних IP-адрес.

Функція очікує як аргументи на два списки:
* список доступних IP-адрес
* список недоступних IP-адрес

Результат роботи функції – вивід на стандартний потік виведення таблиці:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функція нічого не повертає, лише робить print.

Приклад виклику функції
In [6]: reach_ip = ["10.1.1.1", "10.1.1.2"]
In [7]: unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]

In [8]: print_ip_table(reach_ip, unreach_ip)
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

def print_ip_table(reach_ip, unreach_ip):
    print("{:12} {:12}".format("Reachable", "Unreachable"))
    print("{:12} {:12}".format("-----------", "-------------"))
    count_max = len(reach_ip) if len(reach_ip) > len(unreach_ip) else len(unreach_ip)
    count = 0
    while count < count_max:
        print("{:12} {:12}".format(reach_ip[count] if count < len(reach_ip) else "", unreach_ip[count] if count < len(unreach_ip) else ""))
        count += 1
        