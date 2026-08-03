class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n-1,-1,-1):
            take1 = stoneValue[i] - dp[(i+1)%3]

            take2 = float('-inf')
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i+1] - dp[(i+2)%3]

            take3 = float('-inf')
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[(i+3)%3]
                
            dp[i % 3] = max(take1,take2,take3) 
        ans = dp[0]
        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"   