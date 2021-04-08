
T = int(input())

def findNum():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = [0 for _ in range(N)]
    count = 0
    while True:
        for i in range(N):
            if nums[i] == max(nums):
                count += 1
                arr[i] = count
                nums[i] = 0
            if max(nums) == 0:
                count = -1
                break
        if count == -1:
            break
    print(arr[M])


for _ in range(T):
    findNum()




