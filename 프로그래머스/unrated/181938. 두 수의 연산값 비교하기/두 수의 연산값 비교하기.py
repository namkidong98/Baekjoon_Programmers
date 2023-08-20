def solution(a, b):
    a, b = str(a), str(b)
    case1 = int(a + b)
    case2 = int(a) * int(b) * 2
    return case1 if case1 >= case2 else case2