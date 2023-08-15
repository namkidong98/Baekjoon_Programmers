def solution(dots):
    x1, y1 = dots[0]
    dots = dots[1:]
    for i in range(3):
        if dots[i][0] == x1:
            x4, y4 = dots[i]
        if dots[i][1] == y1:
            x2, y2 = dots[i]
    return abs(x1 - x2) * abs(y1 - y4)