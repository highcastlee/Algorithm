import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
grapgh = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # graph는 index x와 연결되어있는 y와의 거리 z (간선)의 모음
    grapgh[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # heapq는 거리가 가까운 노드부터 pop 해준다
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 최단 거리인 상태라면 패스
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드들 체크
        for i in grapgh[now]:
            # 현재 dist에서 다음 노드 거리 추가
            cost = dist + i[1]
            # cost가 다음 노드의 최단거리보다 작으면 다음 노드의 최단거리 갱신함
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 갱신된 다음 노드가 heapq에 추가
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance=max(max_distance, d)

print(count, max_distance)