class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True]*(right+1)
        primes[0]=primes[1]=False
        
        for i in range(2, int(right**0.5)+1):
            if primes[i]:
                for j in range(i*i,right+1,i):
                    primes[j]=False
        prev=0
        ans=[]
        mini=10000000000
        for i in range(left,right+1):
            if primes[i]:
                if i-prev<mini and prev!=0:
                    ans = [prev,i]
                    mini=min(mini,i-prev)
                prev=i
            #print(ans)
        return ans if len(ans)>1 else [-1,-1]
