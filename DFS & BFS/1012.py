from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    if visited[x][y] == True:
        return 0
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        if graph[x][y] == 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
    return 1


for i in range(T):
    M, N, K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for j in range(K):
        a,b = map(int, input().split())
        graph[b][a] = 1

    result = 0

    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1:
                result += bfs(j,k)

    print(result)


