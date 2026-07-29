class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pro = 1
        s = 0
        while n > 0:
            t = n % 10
            s += t
            pro *= t
            n //= 10
        return pro - s
        