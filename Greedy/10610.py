nums = list(map(int, input()))

result = ''

if nums.count(0) == 0 or sum(nums) % 3 != 0:
    result = -1
else:
    nums.sort(reverse=True)
    result = result.join(map(str, nums))

print(result)
