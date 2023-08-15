def solution(polynomial):
    poly_list = polynomial.split()
    const_sum = 0; var_sum = 0
    for char in poly_list:
        if char.endswith('x'):
            coef = char.replace('x', '')
            if coef == '':
                var_sum += 1
            else:
                var_sum += int(coef)
        elif char.isdigit(): # 상수항
            const_sum += int(char)
    
    ans = []
    if var_sum >= 1:
        ans.append('x')
    if var_sum >= 2:
        ans.insert(0, str(var_sum))
    if const_sum >= 1:
        if len(ans) >= 1:
            ans.append(' + ')
        ans.append(str(const_sum))
    return ''.join(ans)