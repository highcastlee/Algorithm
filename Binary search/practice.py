
def binary(array, target, start, end):
    if start > end:
        return
    mid = (start+end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        binary(array, target, start, mid-1)
    else:
        binary(array, target, mid+1, end)

