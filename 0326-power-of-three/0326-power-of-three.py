class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # largest power of 3 is 1162261467 in 32 bit range is 3^19
        return n > 0 and 1162261467 % n == 0
        