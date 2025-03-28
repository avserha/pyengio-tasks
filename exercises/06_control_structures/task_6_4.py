# -*- coding: utf-8 -*-
"""
Завдання 6.4

Список файлів містить імена файлів:
["cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"]

Треба перейменувати файли таким чином:
["cfg_01.txt", "cfg_04.txt", "cfg_08.txt", "cfg_09.txt", "cfg_12.txt", "cfg_15.txt"]

Тобто треба зробити так, щоб після cfg_ завжди було дві цифри. Якщо число менше
10, доповнити до 2 цифр нулями на початку.

Написати код, який перетворює імена файлів у потрібний формат і додає їх до
нового списку result (тест перевірятиме змінну result). Отриманий список
результату вивести на стандартний потік виведення (stdout) за допомогою print.

Вихідний список files не можна змінювати вручну, всі зміни треба зробити за
допомогою Python. Також бажано не прив'язуватись до положення файлу у списку.
"""

files = [
    "cfg_1.txt",
    "cfg_4.txt",
    "cfg_8.txt",
    "cfg_9.txt",
    "cfg_12.txt",
    "cfg_15.txt"
]

result = []
for f in files:
    result.append(f"cfg_{int(f[4:-4]):02d}.txt")

print(result)
