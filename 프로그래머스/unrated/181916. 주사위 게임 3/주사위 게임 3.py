def solution(a, b, c, d):
    num = [a, b, c, d]
    num_set = set(num)
    if len(num_set) == 1:
        return 1111 * a
    elif len(num_set) == 2:
        if num.count(a) == 2:
            p, q = num_set
            return (p+q) * abs(p-q)
        elif num.count(a) == 1:
            return (10 * b + a) ** 2
        else:
            for i in num:
                if num.count(i) == 1:
                    return (10 * a + i) ** 2
    elif len(num_set) == 3:
          for i in num:
                if num.count(i) == 2:
                    ans = 1
                    for j in num_set:
                        if j != i:
                            ans *= j
                    return ans
    else:
        return sorted(num)[0]
    