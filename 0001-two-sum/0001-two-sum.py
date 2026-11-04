class Solution(object):
    def twoSum(self, nums, target):
        
        value1=0
        value2=0
        for i in range(len(nums)):
            if target -nums[i] in nums[i+1:]:
                value1=nums[i]
                value2=target-nums[i]
                return nums.index(value1),nums.index(value2,i+1)