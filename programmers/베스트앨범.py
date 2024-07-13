from collections import defaultdict

def solution(genres, plays):
    answer = []
    plays_genre = defaultdict(list)
    sum_genre_play = defaultdict(int)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        plays_genre[genre].append((i, play))
        sum_genre_play[genre] += play
        
    sum_list = sorted(sum_genre_play.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sum_list:
        tmp = sorted(plays_genre[genre], key=lambda x: x[1], reverse=True)
        print(tmp)
        if len(tmp) >= 2:
            answer.append(tmp[:2])
        else:
            answer.append(tmp[0])

    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]	
print(solution(genres,plays))
    