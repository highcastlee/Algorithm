from collections import deque
import sys
m, n = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j] == 1:
            data.append((graph[i][j], 0, i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

data.sort()
q = deque(data)

count = 0

while q:
    tomato, s, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = tomato
                q.append((tomato, s+1, nx, ny))
    # 마지막 s 값 구하기
    count = s

for i in range(n):
    # 익지 않은 토마토 있을 경우 -1
    if graph[i].count(0):
        count = -1

print(count)



