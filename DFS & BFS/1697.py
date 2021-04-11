from collections import deque

n, k = map(int, input().split())

MAX = 100001
time = [0] * MAX

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            return
        for next in (v-1,v+1,v*2):
            if 0 <= next < MAX and not time[next]:
                time[next] = time[v] + 1
                q.append(next)

bfs()

print(time[k])


# 기존 bfs 풀이 방법 + 시간 테이블 + 이동 계산 3가지 방법
