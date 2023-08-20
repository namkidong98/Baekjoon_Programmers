def solution(a, b):
    case1 = int(str(a) + str(b))
    case2 = int(str(b) + str(a))
    return case1 if case1 >= case2 else case2