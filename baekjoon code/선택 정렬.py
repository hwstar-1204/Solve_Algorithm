#선택 정렬 
nums = [3,4,5,1,2]

for i in range(len(nums)-1):
    min_idx = i #최소값  -> !!! 밑으로 내려가면 인덱스가 계속 고정됨 
    for j in range(i+1,len(nums)):
        if nums[j] < nums[min_idx]:
            min_idx = j 
        #앞에서 가장 작은값이랑 바꾸기 
    nums[i],nums[min_idx] = nums[min_idx],nums[i]

print(nums)