# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# Example 2:
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# Input: 218
# Output: false

import math
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            x = n & (n-1)
            if x==0:
                return 1==1
            else:
                return 1==0
        else:
            return 1==0
