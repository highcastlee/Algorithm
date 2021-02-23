

a, b = input().split()

a2 = ''
b2 = ''
for i in range(2, -1, -1):
    a2 = a2+a[i]
    b2 = b2+b[i]

if int(a2) > int(b2) :
    print(list(a2))
else:
    print(b2)

# 방법 1
# a[::-1] 은 a 문자열을 역순으로 변환

# 방법 2
# a를 list로 만들어서 순서를 뒤집는 list의 reverse()함수 사용
# a,b = map(list, map(str, input().split()))
# a.reverse()
# a = "".join(a)   reverse한 것을 문자열로 변환
