class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val : index
        for i in range(len(nums)):
            temp_num = target - nums[i]
            if temp_num in hashMap:
                lst = [hashMap[temp_num], i]
                return lst
            hashMap[nums[i]] = i
