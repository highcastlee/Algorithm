
n = int(input())


students = []

for i in range(n):
    student = input().split()
    students.append((student[0], int(student[1])))

students.sort(key=lambda student: student[1])
print(students)