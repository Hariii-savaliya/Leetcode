class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            else: continue
        result = []
        c=0
        for n in nums:
            if n==0:
                c+=1
            else:
                result.append(n)
        result.extend([0]*c)
        return result


        