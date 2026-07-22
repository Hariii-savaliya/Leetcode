class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        for num in nums:
            m = min(m , num)
        return m