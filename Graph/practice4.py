from collections import deque
import copy

n = int(input())

times = [0] * (n+1)
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    for j in data[1:-1]:
        graph[j].append(i)
        in_degree[i] += 1

def topology():
    result = copy.deepcopy(times)
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:

            result[i] = max(result[i], result[now]+times[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology()







# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1