
T = int(input())

nums = []

for i in range(T):
    nums.append(int(input()))


def fibonacci(n):
    zero = [1, 0]
    one = [0, 1]
    if n <= 1:
        return
    for i in range(2, n+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    return zero, one

zero , one = fibonacci(40)

for num in nums:
    print("%d %d" % (zero[num], one[num]))


# 해당 문제의 포인트
# 1) 제한 시간이 0.25초로 짧으므로 DP를 써야한다는 힌트
# 2) DP는 단순하게 생각하자면, 재귀함수 대신 배열을 쓴다고 생각하자
# 3) 입력 조건으로 N이 40 이하 자연수 or 0 이므로 40까지 배열 결과를 만드는게 빠르다
# 이 문제는 피보나치에 속으면 안되고, 원하는 결과 값에 초점을 맞추고 풀어야함

