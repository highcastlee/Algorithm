import sys

n = int(input())
sang = list(map(int, sys.stdin.readline().split()))

m = int(input())
nums = list(map(int, sys.stdin.readline().split()))

sang.sort()

def binary(arr, target, start, end):
    if start > end :
        return 0
    mid = (start+end)//2
    if target == arr[mid]:
        return 1
    elif target > arr[mid]:
        return binary(arr, target, mid+1, end)
    else:
        return binary(arr, target, start, mid-1)

for i in range(m):
    print(binary(sang, nums[i], 0, len(sang)-1), end=' ')
