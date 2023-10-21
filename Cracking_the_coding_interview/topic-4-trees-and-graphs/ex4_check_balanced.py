# Leetcode: 110. Balanced Binary Tree

from typing import List, Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.val} (left:{self.left}, right:{self.right})"

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
    

if __name__ == "__main__":
    from ex2_minimal_tree import Solution as BuildTree

    test_case = \
        [-65, -64, -55, -50, -43, -30, -10, 0, 5, 10, 11, 34, 56, 70, 74]
    
    test_tree = BuildTree().sortedArrayToBST(test_case)

    print(test_tree)