# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        r = TreeNode(nums[mid])
        r.left = self.sortedArrayToBST(nums[:mid])
        r.right = self.sortedArrayToBST(nums[mid+1:])

        return r

##############################  logic ##########################
# so in this question the logic is taking the mid values and put then has a root node after that left half array will be left root and right half array will be right root
#continue like that until it form the complete tree
