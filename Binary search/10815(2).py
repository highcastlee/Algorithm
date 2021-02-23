import sys

input()

sang = set(map(int, sys.stdin.readline().split()))

input()

nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    if i in sang:
        print(1, end =' ')
    else:
        print(0, end =' ')

