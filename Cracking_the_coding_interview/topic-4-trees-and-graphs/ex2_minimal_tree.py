# Leetcode 108. Convert Sorted Array to Binary Search Tree

from typing import List, Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.val} (left:{self.left}, right:{self.right})"

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.buildTree(nums)
        # print(root)
        return root
    
    def buildTree(self, lst):
        if lst == []:
            return None
        mid = len(lst)//2
        return TreeNode(lst[mid],self.buildTree(lst[:mid]), self.buildTree(lst[mid+1:]))
    
if __name__ == "__main__":
    # test_case = [
    #     -65, -64, -55, -50, -43, -30, -10, 0, 5, 10, 11, 34, 56, 70, 74
    # ]
    test_case = [1,3]
    Solution().sortedArrayToBST(test_case)
