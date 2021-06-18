from collections import deque


def bfs(x,y):
    q, visited = deque([(x, y)]), set([(x, y)])
    eat_count = 0
    time = 0
    answer = 0
    shark = 2
    # 먹은 걸 체크해서 q를 다시 돌리기 위함
    eat_flag = False
    while q:
        size = len(q)
        q = deque(sorted(q, key = lambda x : (x[0], x[1])))
        for _ in range(size):
            r, c = q.popleft()
            # 현재 위치에서 먹이 있으면 먹음
            if graph[r][c] != 0 and graph[r][c] < shark:
                graph[r][c] = 0
                eat_count +=1
                # 먹은 횟수가 상어 크기과 같으면 크기 + 1
                if eat_count == shark:
                    shark += 1
                    eat_count = 0
                # 먹고 나서 q 초기화하고 그 자리(r,c)에서 다시 탐색
                q, visited = deque(), set([(r, c)])
                eat_flag = True

                # 먹었을 때의 시간 저장
                answer = time

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited:
                    continue
                # 상어 크기 이하일 경우, 이동 가능하므로 q에 추가
                if graph[nr][nc] <= shark:
                    q.append((nr, nc))
                    visited.add((nr,nc))

            # 먹이 먹었으면 break해서 for문 탈출
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

r, c = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            r, c = i, j
            graph[r][c] = 0

print(bfs(r, c))

