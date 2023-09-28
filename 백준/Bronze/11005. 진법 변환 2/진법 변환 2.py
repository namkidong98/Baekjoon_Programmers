number, base = map(int, input().split())
num_alpha = dict(list(zip(range(10, 36), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))) # 알파벳과 10~35를 zip으로 각각 묶어주고 리스트로 변환하고 딕셔너리화한다

ans = '' # 답을 저장하는 문자열

# 자리수 구하기
a = 1; len = 0
while a <= number:
    a *= base
    len += 1
    
# 각 자리수 계산하기    
for i in range(len - 1, -1, -1):
    quotient, number = divmod(number, base ** i) # 몫과 나머지로 분리하되 나머지는 다시 number에 재할당
    if quotient >= 10: # 10 이상의 수는 알파벳으로 변환
        quotient = num_alpha[quotient]
    ans += str(quotient)

print(ans)