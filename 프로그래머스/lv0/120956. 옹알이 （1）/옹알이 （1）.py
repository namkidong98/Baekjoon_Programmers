def solution(babbling):
    result = 0
    possible = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for pos in possible:
            # 빈칸을 안 띄우면 줄어든 글자끼리 붙은 것이 possible의 원소와 일치할 수 있음
            word = word.replace(pos, ' ') 
        if word.strip() == '': # 띄운 빈칸들을 고려해서 좌우 공백을 없애고 빈 string이면
            result += 1
            
    return result
