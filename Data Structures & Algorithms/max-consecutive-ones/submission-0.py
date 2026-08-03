class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxP = 0
        count = 0
        for n in nums:
            if n == 0:
                maxP = max(maxP, count)
                count = 0
            else:
                count += 1
        return max(maxP, count)