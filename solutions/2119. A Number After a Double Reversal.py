class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        j=0
        n=num
        while n>0:
            j=j*10+(n%10)
            n//=10
        n=0
        while j>0:
            n=n*10+(j%10)
            j//=10
        
        return n==num
