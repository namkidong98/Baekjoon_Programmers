def solution(bin1, bin2):
    bin1 = bin1[::-1]; bin2 = bin2[::-1] # 두 이진수를 역순으로 뒤집는다
    carry = 0; idx = 0; result = ''
    while idx < max(len(bin1), len(bin2)):
        if idx < len(bin1):
            a = int(bin1[idx])
        else:
            a = 0
        if idx < len(bin2):
            b = int(bin2[idx])
        else:
            b = 0

        total = a + b + carry
        if total == 3:
            carry = 1; result += '1'
        elif total == 2:
            carry = 1; result += '0'
        elif total == 1:
            carry = 0; result += '1'
        else:
            carry = 0; result += '0'
        idx += 1 # 다음 시행을 위한 인덱스 증가
    
    if carry == 1: # 남은 캐리비트가 있으면 추가하고 리턴
        result += '1'
        #return result[::-1] # 다시 역순으로 뒤집은 str이 최종 답
    
    result = result[::-1] # 다시 역순으로 뒤집은 str이 최종 답
    # result의 맨 앞은 1이 나와야 하니 처리해줘야 한다
    index = result.find('1')
    return result[index:]