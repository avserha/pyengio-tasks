# -*- coding: utf-8 -*-
"""
Завдання 9.5a

Зробити копію функції generate_trunk_config із завдання 9.5

Змінити функцію таким чином, щоб вона повертала не список команд, а словник:
* ключі: імена інтерфейсів, виду 'FastEthernet0/1'
* значення: список команд, який потрібно виконати на цьому інтерфейсі

Перевірити роботу функції на прикладі словника trunk_dict та шаблону
trunk_cmd_list.


Приклад роботи функції
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                    'switchport trunk native vlan 999',
                    'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                    'switchport trunk native vlan 999',
                    'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                    'switchport trunk native vlan 999',
                    'switchport trunk allowed vlan 17']}

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""

trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_dict: dict, trunk_template: list) -> dict:
    result = {}
    for intf in intf_vlan_dict:
        result[intf] = []
        for cmd in trunk_template:
            if cmd.startswith("switchport trunk allowed vlan"):
                vlans = list(map(str, intf_vlan_dict[intf]))
                vlans_str = ",".join(vlans)
                result[intf].append(f"{cmd} {vlans_str}")
            else:
                result[intf].append(cmd)
    return result
