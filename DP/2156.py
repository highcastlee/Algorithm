import sys

n = int(input())

wines = [0]

for i in range(n):
    wines.append(int(sys.stdin.readline().strip()))

d = [0] * 10001

d[1] = wines[1]
if n >= 2:
    for i in range(2, n+1):
        d[i] = max(d[i-1], d[i-2]+wines[i], d[i-3]+wines[i-1]+wines[i])


print(d[n])