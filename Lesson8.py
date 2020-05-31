import time
from timeit import default_timer as timer
import math
import sys
import random

def time_decor(func):
    def wrap_d(*args,**kwargs):
        start=timer()
        func(*args,**kwargs)
        end=timer()
        print(f'Время исполнения - {end-start}')
    return wrap_d

def size_decor(func):
    def wrap_s(*args,**kwargs):
        func(*args,**kwargs)
        print('Обьем памяти - ',sys.getsizeof(size_decor))
    return wrap_s

@time_decor
@size_decor
def gen():
    a=(random.randint(1,100000)for j in range(1,1000000))
    return a


@time_decor
@size_decor
def lst_gen():
    a=[random.randint(1,100000)for j in range(1,1000000)]
    return a



if __name__== '__main__':
    gen()
    print()
    lst_gen()
