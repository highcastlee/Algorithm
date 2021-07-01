import copy
import sys
input = sys.stdin.readline

n = int(input())

case = [[],[],[1],[7],[4],[2,3,5],[6,0,9],[8],[],[]]
# case = [6,2,5,5,4,5,6,3,7,6]

mins = [0] * 101
maxs = [0] * 101

nums = [int(input()) for i in range(n)]

def max(k):
    result = []
    s = ''
    cn = copy.deepcopy(k)
    while cn > 1:
        if cn % 2 == 0:
            result.append(case[2][0])
            cn -= 2
        elif cn > 2:
            result.append(case[3][0])
            cn -= 3
    for i in result:
        s += str(i)
    maxs[k] = int(s)
    return maxs[k]

def min(k):
    result = []
    s = ''
    cn = copy.deepcopy(k)

    n = cn % 7
    if n == 1:
        result.append(case[2][0])
        result.append(case[6][1])
        cn -= 8
    elif n > 0:
        result.append(case[n][0])
        cn -= n
    m = cn // 7
    if m > 0:
        for i in range(m):
            result.append(case[7][0])

    for i in result:
        s += str(i)
    mins[k] = int(s)
    return mins[k]

for i in nums:
    print(min(i), end=' ')
    print(max(i))

