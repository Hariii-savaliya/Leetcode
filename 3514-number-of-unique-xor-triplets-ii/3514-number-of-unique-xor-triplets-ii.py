class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = set(nums)
        pair = [False] * 2048
        triplet = [False] * 2048
        for v1 in val:
            for v2 in val:
                pair[v1 ^ v2] = True
        for v in range(2048):
            if pair[v]:
                for v3 in val:
                    triplet[v ^ v3] = True
        return sum(triplet)


        