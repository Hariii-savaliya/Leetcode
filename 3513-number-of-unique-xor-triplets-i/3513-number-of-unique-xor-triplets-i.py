class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 1
        if n == 2:
            return 2
        if n > 2 and (n & (n - 1)) == 0:
            return 2 * n
        else:
            p = 1
            while p * 2 < n:
                p *= 2
            return 2*p

        
        