
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

answer = []
length = len(stages)
for i in range(1, N + 1):
    count = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = count / length

    answer.append((i, fail))
    length -= count

answer = sorted(answer, key=lambda x: x[1], reverse=True)
result = []
for j in range(N):
    result.append(answer[j][0])
print(result)


