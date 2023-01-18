# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
print('Введите чило для ограничения предела')
N=int(input())
print([el for el in range(20, N) if el % 20 == 0 or el % 21 == 0])