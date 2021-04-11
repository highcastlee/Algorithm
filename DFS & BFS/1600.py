from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())

time = [[[0] *(k+1) for _ in range(w)] for _ in range(h)]

graph = [list(map(int, input().split())) for _ in range(h)]

dx = [-1, 1, 0, 0,2,2,1,1,-2,-1,-2,-1]
dy = [0, 0, -1, 1,1,-1,2,-2,1,2,-1,-2]

def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        x, y, z = q.popleft()
        j = 4 if z == k else 12
        if x == h-1 and y == w-1:
            print(time[x][y][z])
            return
        for i in range(j):
            nx, ny = x+dx[i], y+dy[i]
            nz = z if i < 4 else z+1
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if not graph[nx][ny] and not time[nx][ny][nz]:
                time[nx][ny][nz] = time[x][y][z] + 1
                q.append((nx,ny,nz))
    print(-1)

bfs()
