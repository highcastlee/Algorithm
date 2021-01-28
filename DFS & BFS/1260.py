from collections import deque

n, m, v = map(int, input().split())

graph = [
    [],
    [2, 3, 8],
    [1, 7],
]



graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# ex. 2와 5가 연결일 경우, 배열 각 인덱스에 서로 존재해야하고, 정렬되어야함
for i in range(n+1):
    graph[i].sort()


visited = [False] * (n+1)
result = []

def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')
    for next in graph[x]:
      if not visited[next]:
          dfs(graph, next, visited)


def bfs(graph, y, visited):
    q = deque([y])
    visited[y] = True
    while q:
        k = q.popleft()
        print(k, end=' ')
        for i in graph[k]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(graph, v, visited)

visited = [False] * (n+1)
result = []
print('')
bfs(graph, v, visited)