class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ctow = {}
        wtoc = {}
        words = s.split(' ')
        if len(pattern) != len(words): return False 
        for i in range(len(pattern)):
            ch = pattern[i]
            w = words[i]
            if w in wtoc:
                if wtoc[w] != ch:
                    return False
            else:
                wtoc[w] = ch
            if ch in ctow:
                if ctow[ch] != w:
                    return False
            else:
                ctow[ch] = w
        return True


        