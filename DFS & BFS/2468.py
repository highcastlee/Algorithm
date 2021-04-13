from collections import deque

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,height):
    q = deque()
    q.append((x,y))
    if visited[x][y]:
        return 0
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
    return 1

max_result = 0
for h in range(0, 101):
    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h:
                result += bfs(i,j,h)
    max_result = max(max_result, result)
    visited = [[False] * N for _ in range(N)]


print(max_result)









