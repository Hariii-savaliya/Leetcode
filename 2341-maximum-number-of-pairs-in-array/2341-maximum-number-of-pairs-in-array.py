class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1   
        lc = 0
        for num in freq:
            count += freq[num] // 2
            lc += freq[num
            ] % 2    
        return [count,lc]

        
        