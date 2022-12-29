# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} - {list_of_poly_2}')