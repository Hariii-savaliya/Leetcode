class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        b = e = 0
        freq = {}
        while e < n:
            if s[e] not in freq:
                freq[s[e]] = 1
            else:
                freq[s[e]] += 1
            while freq[s[e]] == 3:
                freq[s[b]] -= 1
                b += 1
            ans = max(ans,e - b + 1)
            e += 1
        return ans