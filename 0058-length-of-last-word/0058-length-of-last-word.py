class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = rstrip(s)
        l = n.split(' ')
        return len(l[-1])
        