#Given a 32-bit signed integer, reverse digits of an integer.
#
#Example 1:
#
#Input: 123
#Output: 321
#
#Example 2:
#
#Input: -123
#Output: -321
#
#Example 3:
#
#Input: 120
#Output: 21
#
#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
#[-231,  231 - 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x not in range(-2**31,2**31):
            return 0
        sign = 1
        if x<0:
            sign = -1
        s = 0
        x = abs(x)
        while x!=0:
            pop = x%10
            x = int(x/10)
            s=s*10+pop
        s*=sign
        if s not in range(-2**31,2**31):
            return 0
        else:
            return s
            
  # faster solution
  
import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x not in range(-2**31,2**31):
            return 0
        sign = 1
        if x > 0:
            digits = int(math.log10(x))+1
        elif x == 0:
            digits = 1
        else:
            digits = int(math.log10(-x))+1
            sign = -1
        s = 0
        x = abs(x)
        for i in range(digits):
            s = s+ int(x/(10**(digits-i-1)))*(10**i)
            x = x-int(x/(10**(digits-i-1)))*(10**(digits-i-1))
        s*=sign
        if s not in range(-2**31,2**31):
            return 0
        else:
            return s
