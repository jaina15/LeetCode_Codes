class Solution:
    def isHappy(self, n: int) -> bool:
        slow,fast = n,n
        while True:
            slow = self.findSquareSum(slow)
            fast = self.findSquareSum(self.findSquareSum(fast))
            if slow == fast:
                break
        if slow==1:
            return True
        return False
    
    def findSquareSum(self, n):
        num=n
        ans=0
        while num>0:
            r=num%10
            ans+=(r*r)
            num//=10
        return ans
