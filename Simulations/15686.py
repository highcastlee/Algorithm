from itertools import combinations

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

chickenLocation = []
houseLocation = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickenLocation.append([i,j])
        elif graph[i][j] == 1:
            houseLocation.append([i,j])

chickenCombination = list(combinations(chickenLocation, m))

result = []

for chicken in chickenCombination:
    total_distance = 0
    for house in houseLocation:
        distance = []
        for i in range(m):
            distance.append(abs(house[0]-chicken[i][0]) + abs(house[1]-chicken[i][1]))
        total_distance += min(distance)
    result.append(total_distance)

print(min(result))






