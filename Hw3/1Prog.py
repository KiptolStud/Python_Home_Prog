# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
number = int(input('Введите размер списка '))
from random import randint

def get_list(number, frst, last):
    return [randint(frst, last) for i in range(number)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

#n = 10
frst = 1
last = 10

mylist = get_list(number, frst, last)
print(mylist)
print(sum_odd_position(mylist))