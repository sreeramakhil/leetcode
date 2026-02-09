class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending =nums[0]
        maxsofar =nums[0]

        for i in range(1, len(nums)):
            maxending =max(nums[i],nums[i]+maxending)
            maxsofar = max(maxsofar , maxending)

        return maxsofar
        
####### sliding window doesn't work because when there are two numbers in the aaray and by using sliding window we have to add those number and find the max values 
