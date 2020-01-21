# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:50:35 2019

@author: I.Kiryushin
"""
import numpy as np
import copy
n = int(input("Введите длину: "))
m = int(input("Введите ширину: "))
print("\n")
#создаем массив m на n из нулей
field = np.array([[0 for i in range(m)] for j in range(n)])

#задаем стартовое расположение клеток
field[1, 1:4] = 1
field[2, 1:4] = 1
field[3, 1:4] = 1

print("Исходный массив. Всего клеток: ",field.sum())
for i in field:
    print(' '.join(map(str, i)))
print("\n")

def c_beh(res, x, y):
#считаем количество клеток вокруг выбранной клетки
    alive = res[x-1:x+2, y-1:y+2].sum() - res[x, y]
    if (alive < 2) or (alive > 3):
        return 0#клетка умерла
    if alive == 3:
        return 1#клетка ожила
#создаем новый массив, в который будем записывать клетки
new_field = copy.deepcopy(field)

#функция поведения клетки; принимает координаты клетки x,y в field


x = 1
y = 1

for i in field[1:-1, 1:-1]:
    for j in i:
        new_val = c_beh(field, x, y)
        if new_val != j:#если значение клетки изменилось, то записываем
            new_field[x, y] = new_val
            new_val = j
        x += 1
    x = 1
    y += 1

field = copy.deepcopy(new_field)

print("Итоговый массив. Всего клеток: ",field.sum())
for i in field:
    print(' '.join(map(str, i)))
print("\n")


