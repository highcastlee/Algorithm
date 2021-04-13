from collections import deque
import copy

M, N, H = map(int,input().split())

graph = [[[] for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        graph[h][n] = list(map(int,input().split()))

box = copy.deepcopy(graph)


q = deque()
for m in range(M):
    for n in range(N):
        for h in range(H):
            if box[h][n][m] == 1:
                q.append((h,n,m))

while q:
    h,n,m = q.popleft()

    if m>0 and box[h][n][m-1] == 0:
        box[h][n][m-1] = box[h][n][m] + 1
        q.append((h,n,m-1))
    if m<M-1 and box[h][n][m+1] == 0:
        box[h][n][m+1] = box[h][n][m] + 1
        q.append((h,n,m+1))
    if n>0 and box[h][n-1][m] == 0:
        box[h][n-1][m] = box[h][n][m] + 1
        q.append((h,n-1,m))
    if n<N-1 and box[h][n+1][m] == 0:
        box[h][n+1][m] = box[h][n][m] + 1
        q.append((h,n+1,m))
    if h>0 and box[h-1][n][m] == 0:
        box[h-1][n][m] = box[h][n][m] + 1
        q.append((h-1,n,m))
    if h<H-1 and box[h+1][n][m] == 0:
        box[h+1][n][m] = box[h][n][m] + 1
        q.append((h+1,n,m))

answer = True
max_result = -1
for h in range(H):
    for n in range(N):
        for m in range(M):
            # 모두 익지 못하는 경우
            if box[h][n][m] == 0:
                answer = -1
            max_result = max(max_result, box[h][n][m])

# 모두 익지 못하는 경우 (0이 하나 이상 존재)
if answer == -1:
    print(-1)
# 처음부터 모두 익은 경우 (가장 큰 값이 1)
elif max_result == 1:
    print(0)
# 최소 며칠 걸리는지 bfs 최대값
else:
    print(max_result-1)
