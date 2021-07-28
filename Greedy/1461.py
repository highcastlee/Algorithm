
n, m = map(int, input().split())

q = list(map(int, input().split()))

list1 = []
list2 = []
for num in q:
    if num < 0 :
        list1.append(num)
    else:
        list2.append(num)

left = sorted(list1)
right = sorted(list2, reverse=True)
# maxnum = max(list1[-1], list2[-1])

result = 0
distance = []
for i in range(len(left) // m):
    distance.append(abs(left[m * i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left) // m) * m]))

right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[m * i])
if len(right) % m > 0:
    distance.append(right[(len(right) // m) * m])

distance.sort()
result = distance.pop()
result += 2 * sum(distance)

# while list1:
#     for i in range(m):
#         x = list1.pop()
#         if i == 0 and x != maxnum:
#             result += x * 2
#         if x == maxnum:
#             result += x
#             maxnum = -1
#         if not list1:
#             break
#
# while list2:
#     for i in range(m):
#         x = list2.pop()
#         if i == 0 and x != maxnum:
#             result += x * 2
#         if x == maxnum:
#             result += x
#             maxnum = -1
#         if not list2:
#             break


print(result)