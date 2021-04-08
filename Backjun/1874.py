import sys
from collections import deque

N = int(input())

initial = [i for i in range(1,N+1)]
nums = deque()
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

stack = []

result = []

for j in initial:
    stack.append(j)
    result.append('+')
    while (len(stack) != 0) & (stack[-1] == nums[0]):
        stack.pop()
        nums.popleft()
        result.append('-')
        if (len(stack) == 0) | (len(nums) == 0):
            break


if len(stack) != 0:
    print('NO')
else:
    for str in result:
        print(str)
