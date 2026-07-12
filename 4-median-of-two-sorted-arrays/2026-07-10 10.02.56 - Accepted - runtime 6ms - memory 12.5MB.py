class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = nums1 + nums2
        result.sort()
        n = len(result)
        median = (result[n//2] + result[(n-1)//2])/2.0
        return median


