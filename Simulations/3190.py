from collections import deque

def info(s):
    if s == 'D':
        return 1
    if s == 'L':
        return -1
    return int(s)

n = int(input())
k = int(input())

apple = [list(map(int, input().split())) for _ in range(k)]

d_count = int(input())

d_info = deque(list(map(info, input().split())) for _ in range(d_count))

graph = [[0] * n for _ in range(n)]

# 첫 자리는 뱀
graph[0][0] = 1

# 사과 위치에 2 표시
for a in apple:
    graph[a[0]-1][a[1]-1] = 2

time = 0

q = deque([[0,0]])

snake = deque([[0, 0]])

dr = [0,1,0,-1]
dc = [1,0,-1,0]
dir = d_info.popleft()
d = 0
r, c = 0, 0

while True:
    # 현재 머리 좌표
    [r, c] = q.popleft()

    # 방향 전환 time일 때
    if dir[0] == time:
        if (d + dir[1]) < 0:
            d = 3
        else:
            d = (d + dir[1]) % 4

        if d_info :
            dir = d_info.popleft()

    nr = r + dr[d]
    nc = c + dc[d]

    # 범위 밖이거나 뱀 몸통이면 종료
    if nr < 0 or nr >= n or nc < 0 or nc >= n or graph[nr][nc] == 1:
        time += 1
        break

    snake.append([nr, nc])
    # 빈 곳이라면, 꼬리 삭제
    if graph[nr][nc] == 0:
        [x, y] = snake.popleft()
        graph[x][y] = 0

    graph[nr][nc] = 1

    q.append([nr, nc])

    time += 1

print(time)