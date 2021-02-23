import sys

n = int(input())

graph = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph.append((a,b))

graph.sort(key = lambda list:(list[0],list[1]))

for i in graph:
    print(i[0], i[1])

