class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax=float('-inf')
        secondMax=float('-inf')
        thirdMax=float('-inf')
        for i in range(0,len(nums)):
            if nums[i]>firstMax:
                thirdMax=secondMax
                secondMax=firstMax
                firstMax=nums[i]
            elif nums[i]>secondMax and nums[i]!=firstMax:
                thirdMax=secondMax
                secondMax=nums[i]
            elif nums[i]>thirdMax and nums[i]!=secondMax and nums[i]!=firstMax:
                thirdMax=nums[i]
        if thirdMax==float('-inf'):
            return firstMax
        else:
            return thirdMax