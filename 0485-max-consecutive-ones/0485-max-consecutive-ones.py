class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        for n in nums:
            if n == 1: 
                cur += 1
                if cur > ans: 
                    ans = cur
            else: cur = 0
        return ans