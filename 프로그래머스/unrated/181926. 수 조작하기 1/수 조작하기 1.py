def solution(n, control):
    n += control.count('w') - control.count('s')
    n += (control.count('d') - control.count('a')) * 10
    return n
