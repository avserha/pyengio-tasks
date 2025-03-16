# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address
"""

ip_str = input("Enter IP address: ")
ip_str = ip_str.split(".")
try:
    ip = list(map(int, ip_str))
    for i in ip:
        if not (0 <= i <= 255):
            ip = False
except:
    ip = False
if len(ip_str) != 4 or ip == False:
    print("Wrong IP address")
else:
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