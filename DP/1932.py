
import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * len(i) for i in graph]


dp[0][0] = graph[0][0]

for i in range(n):
    l = len(graph[i])
    for j in range(l):
        if j == 0:
            dp[i][0] = dp[i-1][0]+graph[i][0]
            continue
        if j == l-1:
            dp[i][j] = dp[i-1][j-1] + graph[i][j]
            continue
        dp[i][j] = max(dp[i-1][j-1]+graph[i][j], dp[i-1][j] + graph[i][j])

print(max(dp[n-1]))
