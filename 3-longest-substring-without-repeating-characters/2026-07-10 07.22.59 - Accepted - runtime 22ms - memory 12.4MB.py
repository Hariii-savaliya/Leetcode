class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = set()
        left = 0
        right = 0
        m = 0

        while (right < len(s)):
            ch = s[right]
            if not ch in l:
                l.add(ch)
                m = max(m, right - left + 1)
                right += 1
            else:
                l.remove(s[left])
                left += 1
        return m
    

        
        