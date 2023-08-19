def solution(before, after):
    dic_b = dict({i: before.count(i) for i in before})
    dic_a = dict({i: after.count(i) for i in after})
    return 1 if dic_a == dic_b else 0