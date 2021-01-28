from collections import deque
import sys
sys.setrecursionlimit(10000)


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    # input()으로 받으면 백준에서는 시간 초과 뜬다
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


visited = [False] * (n+1)

count = 0


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)



# 파이썬에서는 재귀함수가 1000번 이상으로 늘어나는 것을 막고 있다.(Recursion error)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)