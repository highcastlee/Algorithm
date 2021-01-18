
T = int(input())
result = []
for i in range(T):
    H, W, N = map(int, input().split())
    rooms = [0, 1]
    if N % H == 0:
        rooms[0] = H
        rooms[1] = N // H
    else:
        rooms[0] += N % H
        rooms[1] += N // H
    result.append(rooms[0] * 100 + rooms[1])

for j in result:
    print(j)
