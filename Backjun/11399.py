
 # 뽑는 시간이 적은 순으로 정렬하고 그 순서대로 진행


n = int(input())
times = list(map(int, input().split()))

times.sort()

result = 0
for i in range(n):
    result += times[i] * (n-i)

print(result)
