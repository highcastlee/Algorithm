import heapq
import sys

input= sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
#             i[0]은 노드, i[1]은 시간
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
result = 0
for i in distance:
    if (i > 0) & (i < INF):
        count += 1
        result = max(result, i)

print(count, result)