def cal(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    gradient = (x1 - x2) / (y1 - y2)
    return gradient

def solution(dots):
    # case1: 12 34
    a = cal(dots[0], dots[1])
    b = cal(dots[2], dots[3])
    if a == b:
        return 1
    # case2: 13 24
    a = cal(dots[0], dots[2])
    b = cal(dots[1], dots[3])
    if a == b:
        return 1
    # case3: 14 23
    a = cal(dots[0], dots[3])
    b = cal(dots[1], dots[2])
    if a == b:
        return 1
    
    # 여기까지 오면 평행한 경우가 없다는 뜻
    return 0