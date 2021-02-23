import sys

n, m = map(int, input().split())

cake = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(cake)

cake.sort()

while start <= end:
    total = 0
    mid = (start+end)//2
    for x in cake:
        if x > mid:
            total += x - mid
    if total >= m:
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)



