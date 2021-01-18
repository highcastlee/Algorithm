N = int(input())

x = N // 3
y = N // 5

result = []

for i in range(x+1):
    for j in range(y+1):
        if N == (3*i + 5*j):
           result.append(i+j)

answer = 0
if len(result) == 0:
    answer = -1
else:
    answer = min(result)

print(answer)