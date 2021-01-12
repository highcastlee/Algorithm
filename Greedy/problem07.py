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
