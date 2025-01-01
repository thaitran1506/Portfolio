"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

def solution(nums):
    for i in range(0, len(nums)):
        nums[i] = abs(nums[i])
    j = 0
    k = len(nums) - 1
    while k > 0:
        if nums[j] > nums[k]:
            nums[j], nums[k] = nums[k], nums[j]
        k -= 1
    for l in range(len(nums)):
        nums[l] = nums[l]**2


nums = [-4,-1,0,3,10]
print(solution(nums))
print(nums)