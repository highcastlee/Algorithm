# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
#
# start = int(input())
# graph = [[] for i in range(n+1)]
#
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0,start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        # distance값이 이미 더 낮으면 패스~
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[0]는 노드, i[1]은 거리
            # 그 다음 노드까지의 거리 cost
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # now의 다음 노드 거리도 최소로 갱신하고, heapq에 넣는다.
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

































