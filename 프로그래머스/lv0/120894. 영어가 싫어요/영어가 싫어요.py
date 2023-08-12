def solution(numbers):
    num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
              'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    i = 0; ans = ''
    while i <= len(numbers):
        for j in range(1, 6):
            if numbers[i: i + j] in num_dic:
                ans += str(num_dic[numbers[i : i+j]])
                i += 1
        i += 1
    return int(ans)