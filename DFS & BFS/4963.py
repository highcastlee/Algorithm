from collections import deque
import sys

input = sys.stdin.readline


dx = [-1,1,0,0,1,1,0,-1,-1]
dy = [0,0,-1,1,-1,1,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    if graph[x][y] == 0 or visited[x][y] == True:
        visited[x][y] = True
        return 0
    while q:
        x, y = q.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or  ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            q.append((nx,ny))
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h ==0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[False] * (w) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            result += bfs(i,j)

    print(result)






