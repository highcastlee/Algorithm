import sys

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [True] + [False] * n
count = 0


def dfs(x):
    global count
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            count += 1
            dfs(nx)


dfs(1)

print(count)