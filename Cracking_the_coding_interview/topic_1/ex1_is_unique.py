# From Leetcode: 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        Given an array of integers,
        return true only if it contains 
        duplicate elements.
        """
        tmp_dict = {}
        for i in nums:
            try:
                tmp_dict[i]
                return True
            except:
                tmp_dict[i] = 1
        return False


