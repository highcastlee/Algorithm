data = input()

count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))


# 연속된 하나 이상의 숫자를 모두 뒤집는 것은, 다음 자리의 숫자가 달라질 때 카운팅하는 원리
# 0 -> 1 과 1 -> 0 으로 변하는 각각 카운팅 합 중 작은 값을 구한다