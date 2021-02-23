import sys
sys.setrecursionlimit(1111111)

n, m = map(int, input().split())

graph = []

for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

direction = 0

min_visited = n+m
count = 0

def dfs(x, y):
    global count
    global min_visited
    if x == n-1 and y == m-1 :
        min_visited = min(min_visited, count)
        return

    for i in range(1, graph[x][y]+1):
        nx = x + i
        if nx < n and count < min_visited:
            count += 1
            dfs(nx, y)
            count -= 1
        ny = y + i
        if ny < m and count < min_visited:
            count += 1
            dfs(x, ny)
            count -= 1

dfs(0, 0)

print(min_visited)

# 시간초과@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@