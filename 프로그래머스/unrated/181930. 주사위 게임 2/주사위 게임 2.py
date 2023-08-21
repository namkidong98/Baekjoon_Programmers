def solution(a, b, c):
    length = len(set([a, b, c]))
    if length == 1:
        return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    elif length == 2:
        return (a+b+c) * (a**2+b**2+c**2)
    elif length == 3:
        return (a+b+c)