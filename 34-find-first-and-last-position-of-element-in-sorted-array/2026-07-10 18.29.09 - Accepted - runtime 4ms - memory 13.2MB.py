class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            first = nums.index(target)
            nums.reverse()
            last = len(nums)-nums.index(target)-1
            return [first , last]
        else:
            return[-1,-1]  
        