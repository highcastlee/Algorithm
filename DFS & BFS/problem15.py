from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # a번 도시와 연결된 도시들을 묶은 리스트
    graph[a].append(b)

print(graph)

# 거리 초기화
distance = [-1] * (n+1)
# 시작점 x의 거리는 0
distance[x] = 0


q = deque([x])
while q:
    now = q.popleft()
    # now번 도시와 연결된 도시들 next
    for next in graph[now]:
        # 아직 해당 도시 방문 하지 않았을 경우
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)



