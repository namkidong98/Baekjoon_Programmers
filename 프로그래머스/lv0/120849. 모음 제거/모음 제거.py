def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    ans = ''
    for char in my_string:
        if char not in vowel:
            ans += char
    return ans