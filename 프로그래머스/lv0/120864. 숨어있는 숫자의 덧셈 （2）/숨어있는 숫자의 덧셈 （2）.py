def solution(my_string):
    ans = 0
    mult = 1
    my_string = list(my_string)
    my_string.reverse()
    for idx, char in enumerate(my_string):
        if char.isdigit(): # 숫자가 들어오면
            ans += int(char) * mult
            
            if idx +1 < len(my_string) : # 다음 글자가 있으면서
                if my_string[idx+1].isdigit(): # 다음 글자도 숫자이면
                    mult *= 10 # 자리수가 늘어나니 10씩 곱해준다
                    
                else: # 다음 글자가 숫자가 아니면 
                    mult = 1 # 연속되지 않으니 곱해주는 값을 1로 변경
    return ans
                
        