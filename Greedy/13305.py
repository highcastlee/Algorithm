

n = int(input())

length = list(map(int,input().split()))
cost = list(map(int,input().split()))

final = sum(length)

result = 0
currentCost = cost[0]
for i in range(n-1):
    currentCost = min(currentCost, cost[i])
    result += currentCost*length[i]
    final -= length[i]

print(result)
