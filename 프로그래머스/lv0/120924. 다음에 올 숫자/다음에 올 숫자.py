def solution(common):
    test = common[:3] # 앞의 3개를 슬라이싱
    if test[1] - test[0] == test[2] - test[1]: #등차수열이면
        d = test[1] - test[0] # 등차
        return common[-1] + d
    else:
        r = test[1] / test[0]
        return common[-1] * r