import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0
        else:
            graph[i][j] = 1
        print(graph[i][j], end=' ')
    print()
