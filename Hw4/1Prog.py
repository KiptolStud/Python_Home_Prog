#Вычислить число c заданной точностью d in
#Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001
#out
#9.000000

chisl = int(input('Введите число: '))
from decimal import Decimal, getcontext
getcontext().prec = 7
number = Decimal(chisl)
print(number.quantize(Decimal('0.000001')))


