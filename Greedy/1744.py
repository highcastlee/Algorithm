
n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort()
plus = []
minus = []
for i in nums:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

result = 0
while len(plus) >= 2:
    n1 = plus.pop()
    n2 = plus.pop()
    if n1*n2 > n1+n2:
        result += n1*n2
    else :
        result += n1+n2
if len(plus) == 1:
    result += plus.pop()

minus.sort(reverse=True)
while len(minus) >= 2:
    n1 = minus.pop()
    n2 = minus.pop()
    result += n1*n2
if len(minus) == 1:
    result += minus.pop()

print(result)






