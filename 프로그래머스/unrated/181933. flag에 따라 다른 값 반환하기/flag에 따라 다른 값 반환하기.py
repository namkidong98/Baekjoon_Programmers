def solution(a, b, flag):
    flag = '+' if flag else '-'
    string = f"{a} {flag} {b}"
    return eval(string)