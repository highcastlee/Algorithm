from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

in_degree = [0] * (n+1)
graph= [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topology():
    result = []
    q = deque()
    for i in range(1,n+1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology()

