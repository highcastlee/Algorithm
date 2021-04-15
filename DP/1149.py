import sys
sys.setrecursionlimit(100000)

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

p = [[0,0,0] for _ in range(n)]

for k in range(n):
    if k == 0:
        p[k] = data[k]
    else:
        p[k][0] = data[k][0] + min(p[k - 1][1], p[k - 1][2])
        p[k][1] = data[k][1] + min(p[k - 1][0], p[k - 1][2])
        p[k][2] = data[k][2] + min(p[k - 1][0], p[k - 1][1])


print(min(p[n-1][0], p[n-1][1], p[n-1][2]))