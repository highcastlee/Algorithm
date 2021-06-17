
n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph= []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

count = 0


while True:
    if graph[r][c] == 0:
        count += 1
    graph[r][c] = 2
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3
        nx = c + dx[d]
        ny = r + dy[d]
        if graph[ny][nx] == 1 or graph[ny][nx] == 2:
            continue
        else:
            r = ny
            c = nx
            break
    if graph[r][c] == 2:
        nr = r - dy[d]
        nc = c - dx[d]
        if graph[nr][nc] == 1:
            break
        else:
            r = nr
            c = nc

print(count)

