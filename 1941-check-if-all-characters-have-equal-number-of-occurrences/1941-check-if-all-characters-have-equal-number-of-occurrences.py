class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        exp = next(iter(freq.values()))
        for ch in freq:
            if freq[ch] != exp:
                return False
        return True