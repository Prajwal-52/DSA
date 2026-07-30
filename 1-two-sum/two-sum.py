class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            compliment=target-nums[i]
            if compliment in d:
                return [d[compliment],i]
            else:
                d[nums[i]]=i
        return []