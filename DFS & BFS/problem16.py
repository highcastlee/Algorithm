n, m = map(int, input().split())

# 초기 맵 리스트
data = []

# 벽을 설치한 뒤의 맵 리스트
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 or nx < n or ny < m or ny >= 0:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # 벽이 3개가 될 때 temp로 현 data 옮긴 후 virus 전파 시도
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                # count가 3이 되어 return 됐을 때, 그 다음 자리부터 다시 count하며 전체 좌표 체크함
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
