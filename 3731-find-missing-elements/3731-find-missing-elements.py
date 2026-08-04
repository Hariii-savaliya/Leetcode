class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = max(nums)
        b = min(nums)
        ans = []
        s = set(nums)
        for i in range(b+1,a):
            if i not in s:
                ans.append(i)
        return ans