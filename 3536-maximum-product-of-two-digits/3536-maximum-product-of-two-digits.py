class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        d1 = 0
        d2 = 0
        while n > 0:
            d = n % 10
            n = n//10
            if d >= d1:
                d2 = d1
                d1 = d
            elif d >= d2:
                d2 = d
        return d1*d2