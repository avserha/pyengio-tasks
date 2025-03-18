"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_09.py
==============================
10
20
30
40

Потрібно змінити код таким чином, щоб під час виконання коду був такий вивід
$ python task_09.py
==============================
10
******************************
20
******************************
30
******************************
40
==============================
"""
numbers = [10, 20, 30, 40]
print("=" * 30)
for idx, num in enumerate(numbers):
    print(num)
    if idx < len(numbers) - 1:
        print("*" * 30)
print("=" * 30)
