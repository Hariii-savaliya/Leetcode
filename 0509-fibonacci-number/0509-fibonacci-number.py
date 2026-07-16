class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        ans = []
        ans.append(0)
        ans.append(1)
        for i in range(2,n+1):
            ans.append(ans[i-1]+ans[i-2])
        return ans[n]
        