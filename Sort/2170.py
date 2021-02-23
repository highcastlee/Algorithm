import sys

n = int(input())

lines = []
for i in range(n):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort(key=lambda item:item[0])

result = lines[0][1] - lines[0][0]

for i in range(1, n):
    if lines[i-1][1] > lines[i][0]:
        if lines[i-1][1] > lines[i][1]:
            lines[i][0],lines[i][1] = lines[i-1][1], lines[i-1][1]
        elif lines[i][1] >= lines[i-1][1]:
            lines[i][0] = lines[i-1][1]

    result += lines[i][1] - lines[i][0]


print(result)