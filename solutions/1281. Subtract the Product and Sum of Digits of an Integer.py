class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans,p,s=0,1,0
        while n>0:
            r = n%10
            p*=r
            s+=r
            n//=10
        return p-s
