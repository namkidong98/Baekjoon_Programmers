def solution(n):
    i = 1
    while i <= n:
        if i * i == n:
            return 1
        else:
            i += 1
    return 2
    