class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # successor
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reverse
        nums[i + 1:] = reversed(nums[i + 1:])



#################  use lexicographical algorithm for finding the permutation 
