class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            f = []
            for i in range(len(s)):
                f.append((s[i],t[i]))
            setf = set(f)
            if len(setf) == len(set(s)) == len(set(t)):
                return True
            else:
                return False



        

        