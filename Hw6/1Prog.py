#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
#Use comprehension.

from random import sample
# длина списка
len_list = int(input("Ведите число длины списка: "))
# рандомный список
my_list = [i for i in sample(range(1, len_list*2), len_list)]
print("рандомный список: ", my_list)
# cортированный список
sort_list = [my_list[i]
             for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print("cортированный список: ", sort_list)