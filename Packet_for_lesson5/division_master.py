import math
def is_simple_number(n):
    """
    1.Проверяем числа на простоту
    """
    for d in range(2, n + 1):
        if d > math.sqrt(n):
            return True
        if n % d == 0:
            return False



def print_factors(x):
    '''
    2.Нахождение всех делителей
    '''
    print(f'Делители числа {x}:')
    factors=[]
    for i in range(1, x+1 ):
        if x % i == 0:
                print(i,end=' ')
                print()
                factors.append(i)
    return factors


def max_print_factors(n):
    '''
    3.Нахождение максимального простого делителя
    '''
    return print ('Максимальный простой делитель - ',max(list(filter(is_simple_number,print_factors(n)))))




def max_divider(a,b):
    '''
    5.Наибольший общий делитель
    '''
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return print('Наибольший делитель -',a)
