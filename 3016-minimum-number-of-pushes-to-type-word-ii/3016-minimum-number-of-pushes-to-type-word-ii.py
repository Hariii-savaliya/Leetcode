class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = {}
        for w in word:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1
        ans = 0
        arr = sorted(freq.values(),reverse = True)
        for i,f in enumerate(arr):
            ans += f * (i//8 + 1)
        return ans