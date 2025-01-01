"""
Remove Duplicates from Sorted Array

Problem: Remove duplicates from a sorted array such that each element appears only once.
Hint: Use two pointers, one for traversing and the other for placing unique elements.
"""
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0 #hold the position of the unique element
    for j in range(1, len(nums)): #use j to traverse the array
        if nums[j] != nums[i]: #if the value at position j is different from the value at position i, then we find the unique value
            i += 1 #move i by one position so we can store the next unique value
            nums[i] = nums[j] #replace the current ith position with the jth position

    return i+1

nums = [1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
print(nums)