# Leetcode: 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0,1,1]
        for i in range(3, n + 1):
            res.append(sum(res[-3:]))
        return res[n]

""" 
OR

class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1
        
        if n not in self.memo:
            self.memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        
        return self.memo[n]
"""