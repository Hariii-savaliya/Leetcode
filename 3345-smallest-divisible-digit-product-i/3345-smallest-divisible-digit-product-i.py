class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def pod(num):
            p = 1
            while num > 0:
                p *= num % 10
                num //= 10
            return p
        while pod(n) % t != 0:
            n += 1
        return n