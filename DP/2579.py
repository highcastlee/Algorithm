import sys
input = sys.stdin.readline
n = int(input())

nums = [0 for i in range(301)]

for i in range(n):
    nums[i] = int(input())

result = [0 for i in range(301)]

result[0] = nums[0]
result[1] = max(nums[0]+nums[1],nums[1])
result[2] = max(nums[0]+nums[2], nums[1]+nums[2])
for i in range(3, n):
    result[i] = max(result[i-2]+nums[i], result[i-3]+nums[i-1]+nums[i])

print(result[n-1])
