def solution(players, callings):
    player_dic = {player:rank for rank, player in enumerate(players)}
    rank_dic = {rank:player for rank, player in enumerate(players)}
    
    for calling in callings:
        rank = player_dic[calling] # 불린 선수의 현재 순위를 계산
        front_player = rank_dic[rank - 1] # 앞 선수의 이름을 가져옴
        
        #player_dic에서 두 선수의 rank를 변경
        player_dic[calling], player_dic[front_player] = player_dic[front_player], player_dic[calling]
        #rank_dic에서 랭크에 두 선수 이름을 변경
        rank_dic[rank], rank_dic[rank - 1] = rank_dic[rank - 1], rank_dic[rank]
        
    return [rank_dic[i] for i in range(len(players))]