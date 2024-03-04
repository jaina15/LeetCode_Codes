class Solution:
    def pivotInteger(self, n: int) -> int:
        l,r=0,sum(range(n+1))
        for i,num in enumerate(range(1,n+1)):
            r-=num
            if l==r:
                return num
            l+=num
        return -1
