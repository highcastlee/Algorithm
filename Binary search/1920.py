import sys

n = int(input())

store = list(map(int, sys.stdin.readline().split()))

m = int(input())
client = list(map(int, sys.stdin.readline().split()))

def binary(store, target, start, end):
    if start > end :
        return
    mid = (start+end)//2
    if target == store[mid]:
        return 1
    elif target < store[mid]:
        return binary(store, target, start, mid-1)
    else:
        return binary(store, target, mid+1, end)


store.sort()

for order in client:
    if binary(store, order, 0, n-1) :
        print(1)
    else:
        print(0)

