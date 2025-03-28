# -*- coding: utf-8 -*-
"""
Завдання 5.4a

Запросити користувача введення IP-мережі у форматі: 10.1.1.0 255.255.255.0

Потім вивести інформацію про мережу та маску в такому форматі:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Перевірити роботу скрипта на різних комбінаціях мережа/маска.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад роботи завдання:

$ python task_5_4a.py
Enter network address: 10.1.1.0 255.255.255.0

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


$ python task_5_4a.py
Enter network address: 10.1.1.192 255.255.255.240

Network:
10        1         1         192
00001010  00000001  00000001  11000000

Mask:
/28
255       255       255       240
11111111  11111111  11111111  11110000
"""

ip_with_mask = input("Enter network address: ")
ip = ip_with_mask.split(" ")[0].split(".")
mask = ip_with_mask.split(" ")[1].split(".")
print("Network:")
print("{:10}{:10}{:10}{:10}".format(*ip))
ip_bin = list(map(lambda x: int(x), ip))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*ip_bin))
print()
print("Mask:")
mask_bin = list(map(lambda x: int(x), mask))
mask_str = "{:08b}  {:08b}  {:08b}  {:08b}".format(*mask_bin)
print("/", mask_str.count("1"), sep="")
print("{:10}{:10}{:10}{:10}".format(*mask))
print(mask_str)