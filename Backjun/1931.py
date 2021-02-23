import sys

n = int(input())

nums= []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append([x,y])

nums.sort(key=lambda num: num[0])
nums.sort(key=lambda num: num[1])

count = 0
beforeEnd = 0
for start, end in nums:
    if beforeEnd <= start:
        count += 1
        beforeEnd = end

print(count)




