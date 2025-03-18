# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""

with open("ospf.txt", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()
        prefix = parts[1]
        ad_metric = parts[2].strip("[]")
        next_hop = parts[4].strip(",")
        last_update = parts[5].strip(",")
        outbound_interface = parts[6]

        print(f"Prefix                {prefix}")
        print(f"AD/Metric             {ad_metric}")
        print(f"Next-Hop              {next_hop}")
        print(f"Last update           {last_update}")
        print(f"Outbound Interface    {outbound_interface}")
        print()
