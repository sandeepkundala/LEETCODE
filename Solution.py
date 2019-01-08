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
