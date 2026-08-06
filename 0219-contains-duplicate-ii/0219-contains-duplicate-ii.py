class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        w = set()
        for i in range(len(nums)):
            if nums[i] in w:
                return True
            w.add(nums[i])
            if len(w) > k:
                w.remove(nums[i-k])
        return False