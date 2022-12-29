# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число чтобы указать число элементов: '))
numbers = list(n)
print(numbers)
for i in range (len(numbers)):
    random_num = randint(i, n-1)
    temp = numbers[i]
    numbers[i] = numbers[random_num]
    numbers[random_num] = temp

print(numbers)