class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        freq = Counter(s)

        half_freq = {}
        middle = ""
        half_len = 0

        for ch in sorted(freq):
            if freq[ch] % 2:
                middle = ch

            half_freq[ch] = freq[ch] // 2
            half_len += half_freq[ch]

        perms = math.factorial(half_len)
        for cnt in half_freq.values():
            perms //= math.factorial(cnt)

        if k > perms:
            return ""

        left = []

        while half_len:
            for ch in sorted(half_freq):
                if half_freq[ch] == 0:
                    continue

                curr = perms * half_freq[ch] // half_len

                if k <= curr:
                    left.append(ch)
                    half_freq[ch] -= 1
                    perms = curr
                    half_len -= 1
                    break
                else:
                    k -= curr

        left = "".join(left)
        return left + middle + left[::-1]
        