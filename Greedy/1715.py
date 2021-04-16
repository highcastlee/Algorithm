import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    heapq.heappush(nums, int(input()))

if len(nums) == 1:
    print(0)
else:
    ans = 0
    while len(nums) > 1:
        t1 = heapq.heappop(nums)
        t2 = heapq.heappop(nums)
        ans += t1 + t2
        heapq.heappush(nums, t1+t2)
    print(ans)
