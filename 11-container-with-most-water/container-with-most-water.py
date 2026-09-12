class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        marea=0
        while l<r:
            if h[l]<h[r]:
                area=h[l]*(r-l)
            else:
                area=h[r]*(r-l)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
            marea=max(marea,area)
        return marea