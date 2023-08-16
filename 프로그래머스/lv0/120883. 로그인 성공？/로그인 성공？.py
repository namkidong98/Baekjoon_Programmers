def solution(id_pw, db):
    ans = 'fail'
    for i in db:
        if i[0] == id_pw[0]:
            ans = 'wrong pw'
            if i[1] == id_pw[1]:
                ans = 'login'
                
    return ans