data = input()
result = []
sum = 0

for s in data:
    if s.isalpha():
        result.append(s)
    else:
        sum += int(s)
result.sort()
if sum != 0:
    result.append(str(sum))

print(''.join(result))


# 문자는 오름차순, 숫자는 합하여 뒤에 출력
# .isalpha() 사용하여 숫자와 문자 구분
# 숫자는 합하여서 문자 정렬 후 마지막에 추가
# 문자열로 합치는 것은 .join() 함수
