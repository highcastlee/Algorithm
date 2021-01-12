num = list(map(int, input()))

front_sum = 0
back_sum = 0
middle = int(len(num)/2)

for i in range(middle):
    front_sum += num[i]
    back_sum += num[i+middle]

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")


# 문자열 자릿수의 절반을 이용하여 앞부분의 합과 뒷부분의 합 비교