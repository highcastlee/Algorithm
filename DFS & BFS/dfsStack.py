

answer = []

# 재귀
def dfs(graph, node, visited):
    visited[node] = True
    answer.append(node)

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

    dfs(graph, 1, visited)

    return answer

# stack
def dfs2(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited