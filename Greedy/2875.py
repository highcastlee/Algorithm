n, m, k = map(int, input().split())

count = min (n//2, m)
left_g = n - 2 * count
left_b = m - count
left = left_g + left_b

while k > 0:
    if left == 0:
        k = k - 3
        count = count - 1
    else:
        k = k - left
        left = 0

print(count)