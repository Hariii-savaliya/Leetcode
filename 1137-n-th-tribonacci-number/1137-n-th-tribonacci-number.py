class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n==1 or n==2:
            return 1
        ans = [0,1,1]
        for i in range(3,n+1):
            ans.append(ans[i-3] + ans[i-2] +ans[i-1])
        return ans[-1]
        