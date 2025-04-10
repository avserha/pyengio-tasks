# -*- coding: utf-8 -*-
"""
Завдання 5.4b

Все, як у завданні 5.4a, але, якщо користувач ввів адресу хоста, а не адресу
мережі, треба перетворити адресу хоста на адресу мережі та вивести адресу
мережі та маску, як у завданні 5.4a.

Приклад адреси мережі (усі біти хостової частини дорівнюють нулю):
* 10.0.1.0 255.255.255.0
* 190.1.0.0 255.255.0.0

Приклад адреси хоста:
* 10.0.1.1 255.255.255.0 - хост із мережі 10.0.1.0 255.255.255.0
* 10.0.5.195 255.255.255.240 - хост із мережі 10.0.5.192 255.255.255.240

Приклад роботи завдання якщо користувач ввів адресу 10.0.1.1 255.255.255.0,

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Перевірити роботу скрипту на різних комбінаціях хост/маска, наприклад:
    10.0.5.195 255.255.255.240, 10.0.1.1 255.255.255.0

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Підказка: наприклад є адреса хоста у двійковому форматі та маска мережі 28.
Адреса мережі це перші 28 біт адреси хоста + 4 нуля. Тобто, наприклад, адреса
хоста 10.1.1.195/28 у двійковому форматі буде
bin_ip = "0000101000000001000000111000011"

А адреса мережі буде перших 28 символів з bin_ip + 0000 (4 тому що всього в
адресі може бути 32 біти, а 32 - 28 = 4)
00001010000000010000000111000000
"""

ip_with_mask = input("Enter network address: ")
ip_str, mask_str = ip_with_mask.split(" ")
ip_str = ip_str.split('.')
mask_str = mask_str.split('.')

ip = list(map(int, ip_str))
mask = list(map(int, mask_str))

ip_bin = "".join(f"{octet:08b}" for octet in ip)
mask_bin = "".join(f"{octet:08b}" for octet in mask)
network_bin = "".join(ip_bit if mask_bit == "1" else "0" for ip_bit, mask_bit in zip(ip_bin, mask_bin))

network = [int(network_bin[i:i+8], 2) for i in range(0, 32, 8)]
network_str = list(map(str, network))

print("Network:")
print("{:10}{:10}{:10}{:10}".format(*network_str))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*network))
print()

print("Mask:")
prefix = mask_bin.count("1")
print(f"/{prefix}")
print("{:10}{:10}{:10}{:10}".format(*mask_str))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*mask))
