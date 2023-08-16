def solution(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            n += 1
        elif '3' in list(str(i)):
            n += 1
        i += 1
    return n