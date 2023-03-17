class Solution:
    def countEven(self, num: int) -> int:
        c=0
        
        for n in range(1,num+1):
            l=[]
            while n>0:
                l.append(n%10)
                n//=10
            if sum(l)%2==0:
                c+=1
        return c
