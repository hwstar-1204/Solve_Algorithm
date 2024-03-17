# 펠린드롬수

while True:
    nums = list(input())
    mid = len(nums)//2
    
    if not int(nums[0]):
        break
    if len(nums) % 2:
        del nums[mid]

    if nums[:mid] == nums[mid:][::-1]:
        print('yes')
    else:
        print('no')