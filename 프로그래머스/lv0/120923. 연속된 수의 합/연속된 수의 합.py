def solution(num, total):
    if num % 2 != 0: # 홀수인 경우
        std = total // num
        return [ i for i in range(std - (num//2), std + (num // 2) + 1) ]
    else:
        std = int(total / num + 0.5)
        return [ i for i in range(std - (num//2), std + (num//2))]