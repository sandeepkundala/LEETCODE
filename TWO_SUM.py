#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        ls=[]
        for i in range(len(nums)):
            if (target-nums[i] in d):
                if (d[target-nums[i]]!=d[nums[i]]):
                    ls.append(i)
                    ls.append(d[target-nums[i]][0])
                    return(ls)
                elif(len(d[target-nums[i]])>1):
                    return d[target-nums[i]]
