
n , k = map(int, input().split())

num = list(map(int,input()))

stack = []

for i in range(n):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])


for i in range(len(stack)-k):
    print(stack[i],end='')