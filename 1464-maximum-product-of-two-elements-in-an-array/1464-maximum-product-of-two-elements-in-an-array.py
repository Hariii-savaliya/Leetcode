class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        return (m1-1)*(m2-1)

