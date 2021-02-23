from collections import deque

graph = [[]]
for _ in range(4):
    graph.append(deque(map(int, input())))
k = int(input())

# def turn():
#         if dir == 1:
#             if num < 4 and graph[num][2] != graph[num + 1][6]:
#                 graph[num + 1].append(graph[num + 1].popleft())
#             elif num > 1 and graph[num][6] != graph[num-1][2]:
#                 graph[num - 1].append(graph[num - 1].popleft())
#             graph[num].appendleft(graph[num].pop())
#         elif dir == -1:
#             if num < 4 and graph[num][2] != graph[num + 1][6]:
#                 graph[num+1].appendleft(graph[num+1].pop())
#             elif num > 1 and graph[num][6] != graph[num-1][2]:
#                 graph[num-1].appendleft(graph[num-1].pop())
#             graph[num].append(graph[num].popleft())


def rotate_right(num, dir, graph):
    if num == 5:
        return

    if graph[num-1][2] != graph[num][6]:
        rotate_right(num+1, -dir, graph)
        graph[num].rotate(dir)
    else:
        return

def rotate_left(num, dir, graph):
    if num == 0:
        return

    if graph[num+1][6] != graph[num][2]:
        rotate_left(num-1, -dir, graph)
        graph[num].rotate(dir)
    else:
        return

for i in range(k):
    num, dir = map(int, input().split())
    rotate_right(num+1, -dir, graph)
    rotate_left(num-1, -dir, graph)
    graph[num].rotate(dir)

result = 0
for i in range(1, 5):
    nums = [0, 1, 2, 4, 8]
    result += graph[i][0] * nums[i]

print(result)

# 문제 포인트
# 1) rotate 함수로 리스트 회전 간편화
# 2) 해당 리스트 회전하기 전에 다른 리스트 회전 여부 체크 및 진행해야함
# 3) 같은 행위 반복이면, 재귀함수 떠올리기..!

# 로직 빠르게 정리한 후, 구현하는 방식 아이디어에 초첨 맞추기

