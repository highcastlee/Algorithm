def calc(operators, n, exp):
    if n == 3:
        return str(eval(exp))
    if operators[n] == '*':
        ans = eval('*'.join([str(calc(operators, n + 1, e)) for e in exp.split('*')]))
    if operators[n] == '+':
        ans = eval('+'.join([str(calc(operators, n + 1, e)) for e in exp.split('+')]))
    if operators[n] == '-':
        ans = eval('-'.join([str(calc(operators, n + 1, e)) for e in exp.split('-')]))
    return str(ans)


def solution(expression):
    operators = [
        ('+', '-', '*'),
        ('+', '*', '-'),
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('-', '+', '*'),
        ('-', '*', '+'),
    ]
    result = 0
    for i in range(len(operators)):
        answer = int(calc(operators[i], 0, expression))
        result = max(result, abs(answer))

    return result

print(solution('500-100+23*50-100'))
