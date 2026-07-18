class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = max(nums)
        m = min(nums)
        def gcd(self,a,b):
            while b != 0:
                a , b = b , a%b
            return a
        return gcd(self,M,m)        