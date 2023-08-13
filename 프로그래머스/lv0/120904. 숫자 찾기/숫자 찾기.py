def solution(num, k):
    num = list(str(num))
    idx = -1
    for i in num:
        if int(i) == k:
            return num.index(i) + 1
    return -1