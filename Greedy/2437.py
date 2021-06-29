#n입력받기
n=int(input())
#무게 입력받기
weight=list(map(int,input().split()))

#무게 정렬하기
weight.sort()

target=1
#만들 수 없는 수 찾기
for i in weight:
  if target<i:
    break
  target+=i

print(target)
