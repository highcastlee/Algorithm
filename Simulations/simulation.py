n, m = map(int, input().split())
x,y,direction = map(int, input().split())

d = [[0]*m for _ in range(n)]
# 방문한 좌표의 값 = 1
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 순서 : 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계 방향으로 회전하므로 direction은 0 -> 3 -> 2 -> 1 순서(북 서 남 동)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
# 방문한 칸의 수
count = 1
# 회전 수(4일 경우, 모든 방향이 불가능)
turn_time = 0

while True:
    turn_left()
    # 해당 방향으로 갔을 경우의 좌표 값
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        d[x][y] = 1
        count += 1
        turn_time = 0
    else:
        turn_time += 1
    if turn_time == 4:
        # 해당 방향에서 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 해당 좌표가 육지인 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
