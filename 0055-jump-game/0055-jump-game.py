class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r = 0
        for n in nums:
            if r < 0:
                return False
            elif n > r:
                r = n
            r -= 1
        return True
    




        