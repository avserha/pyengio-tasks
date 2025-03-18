# -*- coding: utf-8 -*-
"""
Завдання 12.1

Створити функцію ping_ip_addresses, яка перевіряє чи пінгуються IP-адреси.
Функція очікує як аргумент на список IP-адрес.

Функція має повертати кортеж із двома списками:
* список доступних IP-адрес
* список недоступних IP-адрес

Для перевірки доступності IP-адреси, використовуйте ping (запуск ping через
subprocess). IP-адреса вважається доступною, якщо виконання команди ping
відпрацювало з кодом 0 (returncode). Нюанси: на Windows returncode може
дорівнювати 0 не тільки, коли ping був успішний, але для завдання потрібно
перевіряти саме код. Це зроблено для спрощення тестів.

"""

import subprocess


def ping_ip_addresses(ip_list):
    ip_list_ok = []
    ip_list_not_ok = []
    for ip in ip_list:
        result = subprocess.run(
            ["ping", "-n", "4", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False
        )
        status = result.returncode
        if status == 0:
            ip_list_ok.append(ip)
        else:
            ip_list_not_ok.append(ip)
    return ip_list_ok, ip_list_not_ok