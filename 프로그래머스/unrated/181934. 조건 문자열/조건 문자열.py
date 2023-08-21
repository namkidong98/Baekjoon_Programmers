def solution(ineq, eq, n, m):
    eq = eq.replace("!", '')
    string = f'{n} {ineq}{eq} {m}'
    return int(eval(string))