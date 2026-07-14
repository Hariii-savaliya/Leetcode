class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
         #g1 = gcd of first subsequence
        #g2 = gcd of second subsequence
        @cache
        def solve(i, g1, g2):
            if i == len(nums):
                if g1 == g2: return 1
                else: return 0
            #Skip the elemnet
            skip = solve(i+1, g1, g2)
            #Add in the first
            first = solve(i+1, math.gcd(g1,nums[i]), g2)
            #Add in the second
            second = solve(i+1, g1, math.gcd(g2,nums[i]))
            return (skip+first+second) % (10**9 + 7)
        return solve(0,0,0) - 1
        