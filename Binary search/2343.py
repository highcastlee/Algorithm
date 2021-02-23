import sys

n, m = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))

start = max(nums)
end = sum(nums)


def check(size):
    count = 0
    total = 0
    for i in range(n):
        if total + nums[i] > size:
            count += 1
            print(total + nums[i], size)
            total = 0
        else:
            total += nums[i]
    return count

# while start <= end:
#
#     mid = (start+end)//2
#     if check(mid) <= m :
#         end = mid - 1
#     else:
#         start = mid + 1

print(check(17))



