class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            compliment=target-nums[i]
            if compliment in dict:
                return [dict[compliment],i]
            dict[nums[i]]=i
        return []