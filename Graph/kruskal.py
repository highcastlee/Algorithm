def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int, input().split())
    # 첫 원소 기준 정렬을 위해 cost를 앞으로!
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 생기지 않을 때만 union 수행
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
