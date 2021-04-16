import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

def solution(money):
    count = 0
    for i in reversed(coins):
        if money < i or money == 0:
            continue
        count += money // i
        money = money % i
    print(count)
    return count

solution(k)