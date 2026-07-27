class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set={}
        for i in range(0,len(nums)):
            compliment=target-nums[i]
            if compliment in set:
                return set[compliment],i
            set[nums[i]]=i
        return []