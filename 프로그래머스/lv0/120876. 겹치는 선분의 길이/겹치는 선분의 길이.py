def cal(line1, line2):
    s1, e1 = line1
    len1 = [ i for i in range(s1, e1)]
    s2, e2 = line2
    len2 = [ i for i in range(s2, e2)]

    total = set(len1) & set(len2)
    return total # 교집합을 반환

def solution(lines):
    a = cal(lines[0], lines[1])
    b = cal(lines[1], lines[2])
    c = cal(lines[0], lines[2])
    ans = len(a | b | c)
    return ans