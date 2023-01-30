import operations_rational as op
import sys
import datetime

now = datetime.datetime.now()

def x():
    firstnum = float(input('Введите первое дробное число: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Введите второе дробное число: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выберете операцию: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный ввод')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Неверный ввод')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Результат вычисления {x} {oper} {y} = {res}\n')
        print(str(now),f'Результат {x} {oper} {y} = {res}\n(уже запиан в текстовый файл)' )
        again = input('Вы хотите производить операции с другими числами? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('Вы хотите ипользовать результат последней операции? (Yes/No): ').lower()
            if useresult == 'yes':
                x = res
                continue
            elif useresult == 'no':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()