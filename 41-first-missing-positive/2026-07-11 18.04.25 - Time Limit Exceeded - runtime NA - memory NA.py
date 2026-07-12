class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while (nums[i] != i+1 and 1 <= nums[i] <= len(nums)):
                cp = nums[i]-1
                (nums[i],nums[cp]) = (nums[cp],nums[i])
        for i in range(len(nums)):
            if  nums[i] != i+1:
                return i+1
        else:
            return len(nums)+1  

        