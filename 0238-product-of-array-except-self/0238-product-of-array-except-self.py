class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        suffix = 1
        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
            ans[-1-i] *= suffix
            suffix *= nums[-1-i]
        return ans
        