class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                ans += nums[i]
            else: break
        while ans in s:
            ans += 1
        return ans