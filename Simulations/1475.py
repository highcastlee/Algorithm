import math

N = input()

nums = [0 for _ in range(10)]

for i in N:
    nums[int(i)] += 1

nums[6] = (nums[6]+nums[9])/2
nums[9] = nums[6]

print(math.ceil(max(nums)))


