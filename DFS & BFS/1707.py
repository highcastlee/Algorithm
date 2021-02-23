import sys
sys.setrecursionlimit(222222)
from collections import deque

K = int(input())

q = deque()

def bfs(x):
    color[x] = 1
    q.deque([x])
    visited[x] = True
    while q:
        x = q.popleft()
        c = 3 - color[x]
        for nx in data[x]:
            if color[nx] == 0:
                color[nx] = c
                q.append(nx)
            elif color[nx] == color[x]:
                STOP = True
                break


for i in range(K):
    V, E = map(int, sys.stdin.readline().split())

    data = [[] for _ in range(V+1)]
    for j in range(1, E+1):
        a, b = map(int, sys.stdin.readline().split())
        data[a].append(b)
        data[b].append(a)

    visited = [True] + [False] * V
    color = [0] * (V+1)

    for i in range(1, V+1):
        if not visited[i]:
            bfs(i)



