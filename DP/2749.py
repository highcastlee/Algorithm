import sys
sys.setrecursionlimit(100000)
n= int(input())


result = [0] * (n+1)

def fibonaci(k):
    if k < 3:
        return 1
    if result[k] != 0:
        return result[k]
    result[k] = fibonaci(k-1) + fibonaci(k-2)
    return result[k]


print(fibonaci(n))





