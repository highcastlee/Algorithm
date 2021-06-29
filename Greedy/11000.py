import heapq
import sys
input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

nums.sort(key= lambda x : x[0])

h = []

for i in range(n):
    # 끝나는 시간이 시작 시간보다 작으면 강의실 하나 줄어듦
    if len(h) != 0 and h[0] <= nums[i][0]:
        # 끝나는 시간이 작은 것 우선 pop
        heapq.heappop(h)
    # 끝나는 시간 삽입 (최소 힙)
    heapq.heappush(h, nums[i][1])

print(len(h))

