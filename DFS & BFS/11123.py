from collections import deque

t = int(input())

for i in range(t):
    H, W = map(int, input().split())

    graph = []
    for j in range(H):
        graph.append(list(map(str, input())))

    visited = [[False] * W for _ in range(H)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()

    def bfs(h, w):
        q.append([h, w])
        visited[h][w] = True
        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < W and ny >= 0 and ny < H:
                    if not visited[ny][nx] and graph[ny][nx] == '#':
                        visited[ny][nx] = True
                        q.append([ny, nx])
    result = 0

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph[i][j] == '#':
                bfs(i, j)
                result += 1

    print(result)