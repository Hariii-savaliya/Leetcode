class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans = ""
        i = 0
        j = len(strs) - 1
        while i < len(strs[0]):
            if strs[0][i] == strs[j][i]:
                ans += strs[0][i]
            else:
                break
            i += 1
        return ans

        
        