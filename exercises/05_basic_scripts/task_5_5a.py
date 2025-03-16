# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""

templates = {
    "access": {
        "command": access_template,
        "message": "Enter VLAN number: "
    },
    "trunk": {
        "command": trunk_template,
        "message": "Enter the allowed VLANs: "
    },
}

interface_mode = input("Enter interface mode (access/trunk): ")
interface_type_number = input("Enter interface type and number: ")
vlan_number = input(templates[interface_mode]["message"])


print()
print("interface", interface_type_number)
print(templates[interface_mode]["command"].format(vlan_number))