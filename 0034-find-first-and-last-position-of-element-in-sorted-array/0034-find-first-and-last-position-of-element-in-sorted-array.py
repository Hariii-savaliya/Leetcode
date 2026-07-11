class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            first = nums.index(target)
            last = len(nums)-nums[::-1].index(target)-1
            return [first , last]
        else:
            return[-1,-1]  
        