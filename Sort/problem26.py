import sys
sys.setrecursionlimit(111111)

n = int(input())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
answer = 0
i = 0

def fibo(answer, nums):
    global i
    if i == n-1:
        return
    print(str(answer)+'+='+str(answer)+'+'+str(nums[i]))
    answer += answer + nums[i]
    i += 1
    fibo(answer, nums)

fibo(answer, nums)

print(answer)
