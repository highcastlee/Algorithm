import sys

n = int(input())

k = int(input())

nums = list(map(int, input().split()))

if k >= n:
    print(0)
    sys.exit()

nums.sort(reverse=True)

diff = []
for i in range(1,len(nums)):
    diff.append(nums[i-1]-nums[i])

diff.sort()

for i in range(k-1):
    diff.pop()
result = 0

for i in diff:
    result += i
print(result)
