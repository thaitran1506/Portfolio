def remove_duplicate1(nums):
    if len(nums) == 2:
        return 2

    i = 2 #assuming the first two positions are valid
    for j in range(2, len(nums)):
        print(i, j)
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
        print(nums)
        print(i)
    return i

nums = [1,1,2,3,3,3,4]
print(remove_duplicate1(nums))
print(nums)
