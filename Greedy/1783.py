import math

n, m = map(int, input().split())

visit = 1

if n >= 3:
    if m < 7:
        visit = min(4, m)
    else:
        visit = m - 2
elif n == 2:
    visit = min(4, math.ceil(m/2))
elif n == 1:
    visit = 1

print(visit)



# if n >= 3:
#     if m <= 4:
#         visit = m
#     elif m > 4 and m < 7:
#         visit = 4
#     else:
#         visit = m - 2
# elif n == 2:
#     if m >= 7:
#         visit = 4
#     elif m < 7:
#         visit = math.ceil(m / 2)
# elif n == 1 or m == 1:
#     visit = 1
