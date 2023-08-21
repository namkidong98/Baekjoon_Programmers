def solution(code):
    mode = 0 # 초기 모드는 0으로 시작
    ret = [] # 답을 담을 빈 리스트
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1' and idx % 2 == 0:
                ret.append(code[idx])
            elif code[idx] == '1':
                mode = 1
        else: # mode가 1인 경우
            if code[idx] != '1' and idx % 2 == 1:
                ret.append(code[idx])
            elif code[idx] == '1':
                mode = 0
    return ''.join(ret) if ret else "EMPTY"