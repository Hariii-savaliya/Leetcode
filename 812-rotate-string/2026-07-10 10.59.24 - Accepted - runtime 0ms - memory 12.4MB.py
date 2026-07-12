class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l = len(s)
        if len(goal)!=len(s):
            return False
        for i in range(len(s)):
            new = s[i:] + s[:i]
            if(goal==new):
                return True
                break
        return False