import sys

test = int(input())

for i in range(test):
    n = int(input())
    graph = []
    for j in range(n):
        a, b = map(int, sys.stdin.readline().split())
        graph.append((a,b))

    graph.sort(key = lambda item : item[0])

    count = 1
    min = graph[0][1]

    for i in range(1, n):
        if graph[i][1] < min:
            min = graph[i][1]
            count += 1
    print(count)

    # 시간초과 코드
    # for j in range(graph_y.index(graph_x[0])+1, n):
    #     graph.remove(graph_y[j])
    #
    # for j in range(graph_x.index(graph_y[0])+1, n):
    #     if graph.count(graph_x[j]) > 0:
    #         graph.remove(graph_x[j])
    #
    # print(len(graph))


