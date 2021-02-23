import sys
n = int(input())

house = list(map(int, sys.stdin.readline().split()))
house.sort()

print(house[(n-1)//2])

