
a, b = map(int, input().split())


count = 1
while b > 1:
    if a >= b:
        break
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        b = b//2
    else:
        break
    count += 1

if a == b:
    print(count)
else:
    print(-1)