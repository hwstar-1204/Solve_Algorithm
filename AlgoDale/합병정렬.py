# https://www.algodale.com/algorithms/merge-sort/

# ver1 : list slice
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_list = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_list.append(low_arr[l])
            l += 1
        else:
            merged_list.append(high_arr[h])
            h += 1
        
    merged_list += low_arr[l:]
    merged_list += high_arr[h:]
    return merged_list



a = [95,4,2,40,43,20,12,0,4,6,8,77]
# print(merge_sort(a))



# 최적화 
def merge_sort_2(arr):
    def sort(low, high):
        if high - low < 2:
            return 
        mid = (high + low) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        tmp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1
            
        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i] = tmp[i - low]

    return sort(0,len(arr))

merge_sort_2(a)
print(a)
