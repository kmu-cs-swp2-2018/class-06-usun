#20181690 정유선

import time
import random


#재귀적 구현
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


#반복적 구현
def iterfibo(n):
    space = 0
    now = 1
    past = 1

    if n < 2 :
        return n

    else:
        for i in range(2, n+1):
            past = now
            now += space
            space = past
    return now


while True:
    n = int(input("Enter a number: "))
    if n == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(n)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(n)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(n, fibonumber, ts))
