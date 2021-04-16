
n = int(input())

datas = [input() for _ in range(n)]

# 딕셔너리 관련 함수 사용 문제

def solution(datas):
    dict = {}
    for data in datas:
        l = len(data)-1
        for s in data:
            if s in dict:
                dict[s] += pow(10, l)
            else:
                dict[s] = pow(10, l)
            l -= 1

    nums = sorted(dict.values(),reverse=True)
    result = 0
    k = 9
    for i in nums:
        result += i*k
        k -= 1
    print(result)
    return result


solution(datas)