
direction = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
snake = [[0] * n for _ in range(n)]
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

moves = []

m = int(input())
for _ in range(m):
    num, c = input().split()
    moves.append([int(num), c])


def change_direction(_dir):
    global direction
    if _dir == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


x = 1
y = 1
snake[x-1][y-1] = 1

time = 0
count = 0
tails = [[1, 1]]

while True:
    x += dx[direction]
    y += dy[direction]
    if x <= n+1 and x >= 0 and y <= n+1 and y >= 0 and snake[x-1][y-1] != 1:
        tails.append([x, y])
        snake[x-1][y-1] = 1
        if board[x-1][y-1] == 0:
            tail = tails.pop(0)
            snake[tail[0]-1][tail[1]-1] = 0
    else:
        time += 1
        break
    time += 1
    if count < m and time == moves[count][0]:
        direction = change_direction(moves[count][1])
        count += 1
print(time)
