# -*- coding: utf-8 -*-
"""
Завдання 6.6

Запросити користувача ввести IP-адресу у форматі 10.0.1.1
Залежно від типу адреси (описані нижче), вивести на стандартний потік виведення:
* 'unicast' - якщо перший байт у діапазоні 1-223 (приклад адреси 50.1.1.1)
* 'multicast' - якщо перший байт у діапазоні 224-239 (приклад адреси 224.1.1.1)
* 'local broadcast' - якщо IP-адреса дорівнює 255.255.255.255
* 'unassigned' - якщо IP-адреса дорівнює 0.0.0.0
* 'unused' - у всіх інших випадках

Приклад виконання скрипту:
$ python task_6_6.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6.py
Enter IP address: 224.1.1.1
multicast

$ python task_6_6.py
Enter IP address: 0.0.0.0
unassigned

$ python task_6_6.py
Enter IP address: 255.255.255.255
local broadcast

$ python task_6_6.py
Enter IP address: 250.1.1.1
unused

"""

ip_str = input("Enter IP address: ")
ip_str = ip_str.split(".")
ip = list(map(int, ip_str))
if 1 <= ip[0] <= 223:
    print("unicast")
elif 224 <= ip[0] <= 239:
    print("multicast")
elif ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0:
    print("unassigned")
elif ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255:
    print("local broadcast")
else:
    print("unused")
