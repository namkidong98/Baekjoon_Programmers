from math import factorial as fac

def solution(balls, share):
    return fac(balls) / (fac(balls - share) * fac(share))