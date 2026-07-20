class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in range(1,rowIndex+1):
            prev = ans[i-1]
            curr = prev * (rowIndex - i + 1) / i
            ans.append(curr)
        return ans
        