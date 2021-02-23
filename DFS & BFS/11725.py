import sys
sys.setrecursionlimit(111111)
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [True] + [False] * n

q = deque()

result = [0] * (n+1)

def bfs(graph, v, visited):
    global result
    q.append(v)
    visited[v] = True

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visited[next]:
                result[next] = x
                visited[next] = True
                q.append(next)

bfs(graph, 1, visited)

for i in range(2, n+1):
    print(result[i])
