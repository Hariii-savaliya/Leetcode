class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor = 0
        al0 = True
        for num in nums:
            xor ^= num
            if num != 0: al0 = False
        if al0: return 0
        elif xor != 0: return n
        else: return n-1