
T = int(input())

result= []

for i in range(T):
    x, y = map(int, input().split())
    k = 1
    count = 0
    mid = (x + y) // 2
    next = x

    while next < y:
        print(k)
        next += k
        count += 1
        if next < mid :
            k += 1
        elif next == mid :
            k = k
        else:
            k -= 1

        if k <= 0:
            k = 1
    result.append(count)

for i in result:
    print(i)

#
# 4    0   1   2   3   4  [5]   6   7   8   9   10
#      / 1 /   2   /     3     /   2   / 1 / 1 /
#
#
# 7    0  1  2 [3]  4  5  6  7
#        1   2  /   2    1  1

# 중앙에서 가장 가까운 값보다 낮은 위치에서 이동할 때까지 k값이 계속 증가
# 그 이후로는 k가 1이면 계속 1, 아니면 1이 될 때까지 k가 줄어듦
# 단, 출발이 mid과 같을 때 다음 k = k 이다.



