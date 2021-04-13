from collections import deque
import copy

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

max_result = 0

def virus():
    global max_result
    g = copy.deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = 2
                q.append((nx,ny))
    max_result = max(max_result, countZero(g))

def countZero(g):
    result = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                result += 1

    return result

def setOne(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                setOne(cnt+1)
                graph[i][j] = 0

setOne(0)
print(max_result)


