class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        while n > 0:
            t = n % 2
            ans.append(t)
            n //= 2
        
        return sum(ans)
        