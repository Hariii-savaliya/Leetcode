class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set = []
        left = 0
        right = 0
        m = 0

        while (right < len(s)):
            ch = s[right]
            if not ch in set:
                set.append(ch)
                m = max(m, right - left + 1)
                right += 1
            else:
                set.remove(s[left])
                left += 1
        return m
    

        
        