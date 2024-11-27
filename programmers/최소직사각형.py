def solution(sizes):
    for size in sizes:
        size.sort(reverse=True)
    
    val_1 = max([sizes[i][0] for i in range(len(sizes))])
    val_2 = max([sizes[i][1] for i in range(len(sizes))])
    
    return val_1 * val_2