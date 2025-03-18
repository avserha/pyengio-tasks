"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_02.py
Python is a high-level, interpreted, general-purpose programming language.

Необхідно змінити рядок start_data за допомогою Python таким чином, щоб на
екран було виведено такий рядок (видалити коми та точку):
$ python task_02.py
Python is a high-level interpreted general-purpose programming language

При цьому не можна змінювати рядок start_data вручну, тільки за допомогою Python.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
start_data = start_data.replace(",", "")
start_data = start_data.replace(".", "")
print(start_data)
