import sys

n = int(input())

data = []

for _ in range(n):
    student = sys.stdin.readline().split()
    data.append((student[0], int(student[1]), int(student[2]), int(student[3])))

data = sorted(data, key=lambda student:student[0])
data = sorted(data, key=lambda student:student[3], reverse=True)
data = sorted(data, key=lambda student:student[2])
data = sorted(data, key=lambda student:student[1], reverse=True)

for i in range(n):
    print(data[i][0])


