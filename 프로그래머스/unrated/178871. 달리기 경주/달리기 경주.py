# index 메소드를 사용하는 것은 list를 for문으로 탐색하는 것이기 때문에 시간 복잡도에서 비효율적이다
# for문의 방식이므로 O(n)의 시간복잡도인 반면 딕셔너리를 활용하면 O(1)에 탐색할 수 있다

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