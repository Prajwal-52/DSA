class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        leftQnCount=0
        rightQnCount=0
        leftKnownSum=0
        rightKnownSum=0
        for i in range(0,n):
            if num[i]=='?':
                if i<n//2:
                    leftQnCount+=1
                else:
                    rightQnCount+=1
            else:
                if i<n//2:
                    leftKnownSum+=int(num[i])
                else:
                    rightKnownSum+=int(num[i])
        totalQn=leftQnCount+rightQnCount
        left=2*leftKnownSum+9*leftQnCount
        right=2*rightKnownSum+9*rightQnCount
        if totalQn%2==1:
            return True
        if left==right:
            return False
        else:
            return True