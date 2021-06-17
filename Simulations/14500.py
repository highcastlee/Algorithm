

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

shapeList = [[[0, 1], [0, 2], [0, 3]],
             [[1, 0], [2, 0], [3, 0]],
             [[0, 1], [1, 0], [1, 1]],
             [[1, 0], [2, 0], [2, 1]],
             [[1, 0], [2, 0], [2, -1]],
             [[0, 1], [0, 2], [1, 0]],
             [[0, 1], [0, 2], [1, 2]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 0], [2, 0]],
             [[0, 1], [0, 2], [-1, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[1, 0], [1, 1], [2, 1]],
             [[1, 0], [1, -1], [2, -1]],
             [[0, 1], [-1, 1], [-1, 2]],
             [[0, 1], [1, 1], [1, 2]],
             [[0, 1], [0, 2], [1, 1]],
             [[1, 0], [1, 1], [2, 0]],
             [[1, 0], [1, -1], [2, 0]],
             [[0, 1], [0, 2], [-1, 1]]]

max_summary = 0
summary = 0

for i in range(n):
    for j in range(m):
        for shape in shapeList:
            summary = graph[i][j]

            for k in range(3):
                nx = j + shape[k][1]
                ny = i + shape[k][0]
                if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                    summary += graph[ny][nx]
            max_summary = max(max_summary, summary)

print(max_summary)
