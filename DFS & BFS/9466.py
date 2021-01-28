import sys
sys.setrecursionlimit(111111)

test = int(input())


def dfs(x):
    global team_members
    visited[x] = True
    cycle.append(x)
    choice = case[x]

    if visited[choice]:
        if choice in cycle :
            team_members += cycle[cycle.index(choice):]
        return
    else:
        dfs(choice)

result = []

for i in range(test):
    n = int(input())
    case = [0] + list(map(int, sys.stdin.readline().split()))

    visited =[True] + [False] * n

    team_members = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    result.append(n-len(team_members))


for i in range(test):
    print(result[i])


