def solution(book_time):
    times, rooms = [], []
    for s,e in book_time:
        times.append([change_min(s), change_min(e) + 10])

    times.sort()
    for st, et in times:
        for i, room_end in enumerate(rooms):
            if room_end <= st:
                rooms[i] = et
                break
        else:
            rooms.append(et)
            
    return len(rooms)
                
    
def change_min(time):
    h,m = map(int, time.split(":"))
    return h*60 + m
