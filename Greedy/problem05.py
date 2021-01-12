from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))

result = []
for i in combinations(weights, 2):
    if i[0] != i[1]:
        result.append(i)

print(len(result))

