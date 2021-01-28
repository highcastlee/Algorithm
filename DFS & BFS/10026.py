from collections import deque
import sys

n = int(input())

graph = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * n for _ in range(n)]

q = deque()

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

normal_count = 0
color_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            normal_count += 1

print(normal_count, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            color_count += 1

print(color_count)


