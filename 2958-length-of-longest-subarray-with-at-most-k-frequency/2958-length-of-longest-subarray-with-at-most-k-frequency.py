class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = {}
        ll = 0
        rr = 0
        result = 0
        while rr < n:
            num = nums[rr]
            rr += 1
            if num not in freq:
                freq[num] = 0
            if freq[num] < k:
                freq[num] += 1
            else:
                while nums[ll] != num:
                    num2 = nums[ll]
                    ll += 1
                    freq[num2] -= 1
                ll += 1
            result = max(result, rr - ll)

        return result