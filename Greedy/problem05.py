from itertools import combinations

n, m = map(int, input().split())
weights = list(map(int, input().split()))

result = []
for i in combinations(weights, 2):
    if i[0] != i[1]:
        result.append(i)

print(len(result))


# 번호가 다른 볼링공 중 무게가 서로 다른 A,B의 조합
# combinations를 이용하여 조합 중 무게가 겹치지 않는 것을 구별함